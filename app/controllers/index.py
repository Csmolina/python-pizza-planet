from typing import Tuple
from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import ManagerFactory


class IndexController:

    @staticmethod
    def test_connection() -> Tuple[bool, str]:
        try:
            ManagerFactory.manager('index').test_connection()
            return True, ''
        except (SQLAlchemyError, RuntimeError) as ex:
            return False, str(ex)
