from flask import Flask
from flasgger import Swagger
from worst_movies_api.model import Seeder, db
from worst_movies_api.routes.worst_movies import worst_movies
from swagger_docs.swagger_template import swagger_template

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    swagger = Swagger(app, template=swagger_template)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        Seeder().seed_all_tables()

    app.register_blueprint(worst_movies)

    return app
