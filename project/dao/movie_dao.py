from typing import Optional, List, TypeVar
from sqlalchemy import desc
from werkzeug.exceptions import NotFound
from project.models.movies import Movie
from project.setup.db.models import Base
from .base import BaseDAO

T = TypeVar('T', bound=Base)


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, page: Optional[int] = None, filter=None) -> List[T]:
        stmt = self._db_session.query(self.__model__)
        stmt = stmt.order_by(desc(self.__model__.year))
        if page:

            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()
