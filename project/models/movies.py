from sqlalchemy import Column, String, Integer, ForeignKey
from marshmallow import Schema, fields
from project.setup.db import models


class Movie(models.Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.Integer()
    director_id = fields.Integer()
