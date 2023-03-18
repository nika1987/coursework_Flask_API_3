from typing import Optional

from flask import abort

from project.exceptions import ItemNotFound
from project.models.users import User, UserSchema
from project.dao.main import UserDAO
from project.tools.security import generate_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_by_user_name(self, name):
        return self.dao.get_by_user_name(name)

    def create(self, user_data: dict) -> str:
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

    def update(self, user_data: dict, user_id: int) -> str: # 2 пароля должно найти
        
        try:
            user_data['password'] = generate_password_hash(user_data['password'])  # перезаписываем пароль пользователя
            self.dao.update_user(user_id, user_data)
            return "Обновлено успешно"
        except Exception as e:
            print(e)
            return "Не удалось обновить данные"
