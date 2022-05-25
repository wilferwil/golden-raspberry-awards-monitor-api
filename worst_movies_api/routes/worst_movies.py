''' Route declaration module. '''
import json
from flask import Blueprint, Response
from flasgger.utils import swag_from
from worst_movies_api.controllers.worst_movies_controller import WorstMoviesController
from swagger_docs.worst_movies_specs import worst_movies_specs

worst_movies = Blueprint('worst_movies', __name__)

@worst_movies.route("/worst_movies", methods=['GET'])
@swag_from(worst_movies_specs, methods=['GET'])
def get_worst_movies():
    ''' Worst movie route declaration and controller call. '''
    worst_movies_rank = WorstMoviesController().get_worst_movies_rank()
    return Response(
        response=json.dumps(worst_movies_rank),
        status=200,
        headers={'Content-Type': 'application/json'})
