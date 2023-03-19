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

    def create_user(self, user_data: dict) -> User:
        entity = User(**user_data)
        self._db_session.add(entity)
        self._db_session.commit()
        return entity

    def get_one(self, uid):
        return self._db_session.query(User).get(uid)

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).first()

    def get_by_user_name(self, name):
        return self._db_session.query(User).filter(User.name == name).first()

    def update_user(self, user_id: int, user_data: dict) -> User:
        user_found = self.get_by_id(user_id)
        if user_data.get('email') is not None:
            user_found.email = user_data['email']
        if user_data.get('password') is not None:
            user_found.password = user_data['password']
        if user_data.get('name') is not None:
            user_found.name = user_data['name']
        self._db_session.commit()
        return user_found

