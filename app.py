import csv
import json
from flask import Flask, request

app = Flask(__name__)

def movie_filter(genre):
    filename = 'imdb-movie-data.csv'
    response = []

    with open(filename) as csvfile:
        csv_content = csv.DictReader(csvfile)
        
        for movie in csv_content:
            genres = movie['Genre'].lower().split(',')
            if genre.lower() in genres:
                response.append(movie)

        return response

@app.route("/")
def root():
    genre = request.args.get("genre", '')
    response = movie_filter(genre)
    return json.dumps(response)
    
@app.route("/<genre>")
def movie_by_single_genre(genre):
    response = movie_filter(genre)
    return json.dumps(response)

if __name__ == "__main__":
    app.run(port=8080)




