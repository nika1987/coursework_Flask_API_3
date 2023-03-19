from typing import Optional

import jwt
from flask import abort

from project.exceptions import ItemNotFound
from project.helps.constans import JWT_SECRET, JWT_ALGORITHM
from project.models.users import User, UserSchema
from project.dao.main import UserDAO
from project.tools.security import generate_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_item(self, pk: int) -> User:
        """
        Метод для получения пользователя по id
        """
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        """
        Метод возвращает всех пользователей

        """
        return self.dao.get_all(page=page)

    def get_one(self, uid: int) -> User:
        """
        Метод для получение одного пользователя
        """
        return self.dao.get_one(uid)

    def get_by_email(self, email: str) -> User:
        """
        Метод для получения пользователя по емайл
        """
        return self.dao.get_by_email(email)

    def get_by_token(self, token: str) -> User:
        """
        Метод для получения пользователя по токену

        """
        user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return self.get_by_email(user['email'])

    def get_by_user_name(self, name: str) -> User:
        """
        Метод для получения пользователя по имени

        """
        return self.dao.get_by_user_name(name)

    def create(self, user_data: dict) -> str:
        """
        Метод добавления нового пользователя
        """
        if self.dao.get_by_email(user_data.get('email')):
            return abort(400, 'Пользователь с таким именем ужe cуществует в базе данных')
        try:
            user_data['password'] = generate_password_hash(user_data['password'])
            create_user = self.dao.create_user(user_data)
            user_dict = UserSchema().dump(create_user)
            user_dict.pop('password')
            return user_dict
        except Exception as e:
            print(e)
            return "Не удалось сгенерировать пароль пользователя"

    def update_user(self, token: str, user_data: dict) -> None:
        """
        Метод обновление пользователя по токену

        """
        user = self.get_by_token(token)
        self.dao.update_user(user.id, user_data)

    def update_password(self, data: dict, email: str) -> None:
        """
        Метод обновления пароля пользователя

        """
        user = self.get_by_email(email)
        data['password'] = generate_password_hash(data['password'])
        self.dao.update_user(user.id, data)
