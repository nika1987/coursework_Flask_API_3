from sqlalchemy import Column, String
from marshmallow import Schema, fields
from project.setup.db import models


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    name = fields.String(required=True)
