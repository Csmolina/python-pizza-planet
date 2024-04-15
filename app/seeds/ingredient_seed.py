from app.repositories.managers import ManagerFactory
import random
from app.repositories.models import Ingredient
from .utils import generators

def add_ingredients():
  new_ingredient =  generators.create_ingredients()
  for ingredient in new_ingredient:
    ManagerFactory.manager('ingredient').create(ingredient)

def get_ingredients():
  ingredients_return = []
  all_ingredients = ManagerFactory.manager('ingredient').get_all()
  ingredients_num = random.randint(1, 10)
  selected_ingredients = random.sample(all_ingredients,ingredients_num)
  for ingredient in selected_ingredients:
    modeled_ingredient = Ingredient(**ingredient)
    if modeled_ingredient not in ingredients_return:
      ingredients_return.append(modeled_ingredient)
  return ingredients_return