from sqlalchemy import Column, String, Integer
from marshmallow import Schema, fields

from project.setup.db import models


class User(models.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(String(255))


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String(required=True)
    surname = fields.String(required=True)
    favorite_genre = fields.String(required=True)
