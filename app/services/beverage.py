from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from ..controllers import BeverageController
from .base import BaseService

beverage = Blueprint('beverage', __name__)
service = BaseService(BeverageController)

@beverage.route('/', methods=POST)
def create_beverage():
    return service.create()

@beverage.route('/', methods=GET)
def get_beverages():
    return service.get_all()

@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return service.get_by_id(_id)

@beverage.route('/', methods=PUT)
def update_beverage():
    return service.update()