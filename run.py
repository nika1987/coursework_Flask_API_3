from project.config import config
from project.models.genres import Genre
from project.models.directors import Director
from project.models.movies import Movie
from project.models.users import User
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Movie": Movie,
        #"User": User,
        #"Director": Director
    }


app.run(debug=True)
