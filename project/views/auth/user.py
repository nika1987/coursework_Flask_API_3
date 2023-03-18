from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service

api = Namespace('user')


@api.route('/user')
class UsersView(Resource):
    def get(self):
        """
        Получаем всех пользователей
        """
        return user_service.get_all()

    def post(self):
        """
        Добавляем нового пользователя

        """
        user_data = request.json
        return user_service.create(user_data)


@api.route('/<int:user_id>/')
class UserView(Resource):
    def get(self, user_id: int):
        """
        Получаем пользователя по id

        """
        return user_service.get_one(user_id)

    def patch(self, user_id: int):
        """
        Обновляем пользователя

        """
        user_data = api.payload
        user_data['id'] = user_id
        user_service.update(user_data)
        return None, 200


@api.route('/password')
class UserView(Resource):
    def put(self):
        data = request.json
        """
        Добавляем пользователя
        """
        email = data.get("email")
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        user = user_service.get_user_by_email(email)

        if user_service.compare_passwords(user.password, old_password):
            user_service.update_password({
                "id": user.id,
                "password": new_password
            })
            return "Password changed successfully", 201
        else:
            return "Password did not changed", 400
