from tkinter.scrolledtext import example

from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie: Model = api.model('Продукт', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название'),
    'description': fields.String(required=True, max_length=1000, example='Описание'),
    'trailer': fields.String(required=True, max_length=1000),
    'year': fields.Integer(required=True, example=2019),
    'rating': fields.Integer(required=True, example=5),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1)
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='ФИО')
})
