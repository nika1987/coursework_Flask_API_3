from .genres import api as genres_ns
from .movie import movie_ns
from .directors import api as directors_ns


__all__ = [
    'genres_ns',
    'movie_ns',
    'directors_ns'
]
