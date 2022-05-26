''' Worst movie endpoint testing. '''
import json

def test_get_worst_movies_status_200(client):
    ''' Test worst movie expecting 200 status code return. '''
    response = client.get('/worst_movies')
    assert response.status_code == 200

def test_get_worst_movies_json_text(client):
    ''' Test worst movie expecting specific pre-calculated json. '''
    response = client.get('/worst_movies')
    expected_return = {
        "min": [
            {
                "producer": "Joel Silver",
                "interval": 1,
                "previousWin": 1990,
                "followingWin": 1991
            },
            {
                "producer": "Bo Derek",
                "interval": 6,
                "previousWin": 1984,
                "followingWin": 1990
            }
        ],
        "max": [
            {
                "producer": "Matthew Vaughn",
                "interval": 13,
                "previousWin": 2002,
                "followingWin": 2015
            },
            {
                "producer": "Buzz Feitshans",
                "interval": 9,
                "previousWin": 1985,
                "followingWin": 1994
            }
        ]
    }
    assert response.text == json.dumps(expected_return)

def test_inexistent_endpoint_404(client):
    ''' Test an inexistent endpoint expecting 404 status code return. '''
    response = client.get('/inexistent_endpoint')
    assert response.status_code == 404

def test_get_worst_movies_wrong_http_verb_405(client):
    ''' Test worst movies endpoint with wrong http verb. '''
    response = client.post('/worst_movies')
    assert response.status_code == 405