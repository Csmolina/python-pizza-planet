from ..repositories.managers import ManagerFactory
from .base import BaseController


class SizeController(BaseController):
    manager = ManagerFactory.manager('size')
