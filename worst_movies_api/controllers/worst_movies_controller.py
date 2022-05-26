''' Worst movie controller module. '''
import pandas as pd
from worst_movies_api.model import db

class WorstMoviesController:
    ''' Worst movie controller class. '''

    def get_worst_movies_rank(self):
        ''' Get smallest and largest intervals between winners of worst movie category. '''
        gra_movies = self.retrieve_gra_worst_movie_winners(db)
        gra_movies = self.prepare_movies_data(gra_movies)
        gra_movies = self.calculate_year_range_between_win(gra_movies)

        shortest_gra = gra_movies.nsmallest(1, 'interval').to_dict('records')
        longest_gra = gra_movies.nlargest(1, 'interval').to_dict('records')

        return self.summarize_winner_overview(shortest_gra, longest_gra)

    @classmethod
    def retrieve_gra_worst_movie_winners(cls, db):
        ''' Retrieve only GRA worst movie winners from the database. '''
        with db.engine.connect() as conn:
            query = 'SELECT * FROM worst_movies WHERE winner = "yes";'
            worst_movies = pd.read_sql_query(query, conn)
            conn.close()

        return worst_movies

    @classmethod
    def prepare_movies_data(cls, gra_movies):
        ''' Prepare retrieved movie data. '''
        gra_movies['producer'] = gra_movies['producers'].str.replace(' and ',', ')
        gra_movies.drop(columns=['producers'], inplace=True)
        gra_movies['producer'] = gra_movies['producer'].str.split(',')
        gra_movies = gra_movies.explode('producer')
        gra_movies['producer'] = gra_movies['producer'].str.strip()
        gra_movies.loc[gra_movies.producer == '', 'producer'] = None
        gra_movies = gra_movies.dropna(subset = ['producer'])
        gra_movies = gra_movies[gra_movies.producer.duplicated(keep=False)]

        return gra_movies

    @classmethod
    def calculate_year_range_between_win(cls, gra_movies):
        ''' Calculate year interval between movies by consecutive winners. '''
        gra_movies.sort_values(['producer', 'year'], ascending=[False, False], inplace=True)

        previous_win = gra_movies['producer'] == gra_movies['producer'].shift(-1)
        gra_movies.loc[previous_win, 'previousWin'] = gra_movies['year'].shift(-1)

        gra_movies.loc[previous_win, 'interval'] = gra_movies['year'] - gra_movies['previousWin']

        gra_movies.rename(columns={"year": "followingWin"}, inplace=True)
        gra_movies = gra_movies[['producer', 'interval', 'previousWin', 'followingWin']]

        gra_movies = gra_movies.astype({"previousWin": 'Int64', "interval": 'Int64'})

        return gra_movies

    @classmethod
    def summarize_winner_overview(cls, shortest_gra, longest_gra):
        ''' Summarize winners data from worst movie category. '''
        return {
            'min': shortest_gra,
            'max': longest_gra
        }
