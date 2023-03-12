
from project.config import DevelopmentConfig
from project.server import create_app
from project.setup.db import db
from project.models.users import User
from project.models.movies import Movie
from project.models.directors import Director
from project.models.genres import Genre

if __name__ == '__main__':
    with create_app(DevelopmentConfig()).app_context():
        db.create_all()
