from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import user_service
from project.decorater import user_required
from project.setup.api.models import user


api = Namespace('users')


@api.route('/')
class UsersView(Resource):
    @user_required
    @api.marshal_with(user, code=200, description="OK")  # сериализация
    def get(self):
        """
        Получить информацию о пользователе
        """

        token = request.headers["Authorization"].split('Bearer ')[-1]
        print(token)
        user_data = user_service.get_by_token(token)
        return user_data

    @user_required
    def patch(self):
        """
        Обновляем частичные данные пользователя
        """
        token = request.headers['Authorization'].split('Bearer ')[-1]
        data_user = request.json
        user_service.update_user(token, data_user)
        return 'user data updated', 200


@api.route('/password/')
class UserView(Resource):

    def put(self):
        """
        Меняем пароль пользователя
        """

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        user = user_service.get_by_token(token)
        data_passwords = request.json
        if data_passwords['password_1'] != data_passwords['password_2']:
            user_service.update_password({'password': data_passwords['password_2']}, user.email)
            return 'password updated', 200
        else:
            return 'error password updated', 400
