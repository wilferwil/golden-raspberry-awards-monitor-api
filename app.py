import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class WorstMovie(db.Model):
    __fillable = ['year','title','studios','producers','winner']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.SmallInteger())
    title = db.Column(db.String(255))
    studios = db.Column(db.String(255))
    producers = db.Column(db.String(255))
    winner = db.Column(db.Enum('no', 'yes'))

    def seed(self):
        worst_movies = pd.read_csv('api/storage/movielist.csv', lineterminator='\n', sep=';')
        worst_movies = worst_movies[self.__fillable]
        worst_movies['winner'] = worst_movies['winner'].fillna('no')
        worst_movies = [WorstMovie(**movie) for movie in worst_movies.to_dict('records')]
        db.session.bulk_save_objects(worst_movies)
        db.session.commit()

db.create_all()
WorstMovie().seed()

@app.route("/worst_movies", methods=['GET'])
def worst_movies():
    return "Starting the project."
