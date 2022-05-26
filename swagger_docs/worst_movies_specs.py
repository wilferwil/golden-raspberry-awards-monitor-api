worst_movies_specs = {
    "tags": [
        {
            "name": "worst_movies",
            "description": ""
        }],
    "summary": "Get the producer with the longest gap between two consecutive awards, and the fastest between two awards.",
    "description": "Get Golden Raspberry Awards consecutive winners. The annual event that awards the worst films of the year.",
    "operationId": "worstMovies",
    "produces": [
        "application/json"
    ],
    "responses": {
        "200": {
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
    }
}
