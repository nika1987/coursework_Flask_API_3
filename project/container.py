from project.dao import GenresDAO
from project.dao.main import DirectorsDAO
from project.dao.movie_dao import MoviesDAO

from project.services import GenresService
from project.services.directors_service import DirectorsService
from project.setup.db import db
from project.services.movie_service import MovieService
# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
