from sqlalchemy import Column, String
from marshmallow import Schema, fields

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    name = fields.String(required=True)
