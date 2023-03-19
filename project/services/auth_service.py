import calendar
import datetime

import jwt
from flask import abort

from project.helps.constans import JWT_SECRET, JWT_ALGORITHM
from project.services.users_service import UserService
from project.tools.security import check_passwords


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, email: str, password: str, is_refresh: bool = False) -> dict:
        """
        Метод создает(генерирует) access_token
        :param email: емайл пользователя
        :param password: пароль пользователя
        :return: словарь с парой токенов
        """
        user = self.user_service.get_by_email(email)
        if user is None:
            raise Exception("User not found")
        if not is_refresh:
            if not check_passwords(user.password, password):
                abort(400, "Неверный пароль или емайл")
        data = {
            "email": user.email,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        data["exp"] = calendar.timegm(min30.timetuple())
        assert_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)
        return {"access_token": assert_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token: str) -> dict:
        """
        Метод для обновления access_token с помощью refresh_token
        """
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data.get("email")

        user = self.user_service.get_by_email(email=email)

        if user is None:
            abort(404, "User not found")
        return self.generate_token(email, user.password, is_refresh=True)
