from project.dao.base import BaseDAO
from project.models.genres import Genre

from project.models.directors import Director
from project.models.users import User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class UserDAO(BaseDAO[User]):
    __model__ = User
