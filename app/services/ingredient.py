from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from ..controllers import IngredientController
from .base import BaseService
ingredient = Blueprint('ingredient', __name__)
service = BaseService(IngredientController)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return service.create()

@ingredient.route('/', methods=PUT)
def update_ingredient():
    return service.update()

@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return service.get_by_id(_id)

@ingredient.route('/', methods=GET)
def get_ingredients():
    return service.get_all()
