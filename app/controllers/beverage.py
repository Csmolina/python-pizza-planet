from ..repositories.managers import ManagerFactory
from .base import BaseController

class BeverageController(BaseController):
    manager = ManagerFactory.manager('beverage')