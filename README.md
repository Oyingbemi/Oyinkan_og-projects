# Welcome to My Imdb Api
This is a Flask application that filters movies from a CSV file based on the genre provided.

The movies_filter function takes a genre as an argument and returns a list of movies that match the genre. If the genre argument is None, it returns all the movies in the CSV file.

## Task
I am to  create a backend API to allow a user to search for a movie search by genre.
## Description
Import the necessary modules/libraries: csv, json, and Flask.

Create an instance of the Flask class and assign it to the app variable.

Define a function called get_movies_by_genre that takes a genre as an argument and returns a list of movies that belong to that genre. The function reads the data from the movies.csv file and returns the rows that match the specified genre.

Create several Flask routes that map to different URLs. Each route invokes the get_movies_by_genre function with a different genre, and returns the resulting list of movies as a JSON response. For example, the /action route returns all action movies, and the /drama route returns all drama movies.

The root route takes an optional genre argument from the URL query string and returns the movies that belong to that genre as a JSON response. If the genre argument is not provided, the route returns a message asking the user to provide a genre.

Finally, the code checks if the script is being run as the main module and starts the Flask application on port 8080.

This code provides a basic structure for building a REST API that serves movie data.

## Installation
All the necessary installations are already embedded in the Qwasar.io interface which include flask, json, python. The interface is really user friendly

## Usage
The API can be used by sending a GET request to the endpoint, either "/" or "/<genre>", where <genre> is the genre of the movie that you want to retrieve. If you send the request to "/", you need to provide a genre in the query string parameter, for example "/?genre=comedy".

For example, if you want to retrieve all action movies, you can send a GET request to "/action". If you want to retrieve all movies of a specific genre, you can send a GET request to "/?genre=<genre>", where <genre> is the genre that you want to retrieve.

The response of the API will be in JSON format, containing a list of dictionaries, where each dictionary represents a movie with its attributes.
```

### The Core Team
OGUNGBEMI OYINKANSOLA A

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
