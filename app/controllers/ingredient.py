from ..repositories.managers import ManagerFactory
from .base import BaseController


class IngredientController(BaseController):
    manager = ManagerFactory.manager('ingredient')
