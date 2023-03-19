import functools

import jwt
from flask import request, abort, current_app
from project.helps.constans import JWT_SECRET, JWT_ALGORITHM


def user_required(func):
    """
    Проверка кем является пользователем

    """

    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            abort(401, e)

        return func(*args, **kwargs)

    return wrapper
