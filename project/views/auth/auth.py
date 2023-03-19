from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

auth_new_ns = Namespace('auth')


@auth_new_ns.route('/register')
class Auth(Resource):
    def post(self):
        """
        Регистрация пользователя по емайл и паролю
        """
        data = request.json

        email = data.get('email')
        password = data.get('password')

        if None in [email, password]:
            return "", 400

        user_service.create(data)

        return "", 201


@auth_new_ns.route('/login')
class LoginView(Resource):
    def post(self):
        data = request.json
        """
        Метод аутенфикации пользователя
        {
       "access_token": "qwesfsdfa",
       "refresh_token": "kjhgfgjakda",
        }
            """
        email = data.get('email')
        password = data.get('password')
        if not all([email, password]):
            return "", 400

        tokens = auth_service.generate_token(email, password)
        return tokens, 201

    def put(self):
        data = request.json
        """
        Получение нового access_token 
        """
        token = data.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)

        return tokens, 200
