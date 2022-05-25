''' Model module to handle the GRA movie data. '''
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
db = SQLAlchemy()

class Base(db.Model):
    ''' Base class with default fields to all database tables. '''
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class Seeder():
    ''' Seeder class to populate the api tables. '''
    __abstract__ = True

    @classmethod
    def seed_all_tables(cls):
        ''' Seed tables for the first use and api testing. '''
        WorstMovie().seed()

class WorstMovie(Base):
    ''' Worst movie model class. '''
    __tablename__ = 'worst_movies'
    __fillable = ['year','title','studios','producers','winner']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.SmallInteger())
    title = db.Column(db.String(255))
    studios = db.Column(db.String(255))
    producers = db.Column(db.String(255))
    winner = db.Column(db.Enum('no', 'yes'))

    def seed(self):
        ''' Seed Worst Movie table with data provided via CSV. '''
        movies_path = 'worst_movies_api/storage/movielist.csv'
        worst_movies = pd.read_csv(movies_path, lineterminator='\n', sep=';')
        worst_movies = worst_movies[self.__fillable]
        worst_movies['winner'] = worst_movies['winner'].fillna('no')
        worst_movies = [WorstMovie(**movie) for movie in worst_movies.to_dict('records')]
        db.session.bulk_save_objects(worst_movies)
        db.session.commit()
