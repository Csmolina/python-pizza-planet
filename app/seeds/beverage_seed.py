import random
from app.repositories.managers import ManagerFactory
from app.repositories.models import Beverage
from .utils import generators

def add_beverages():
  new_beverage =  generators.create_beverages()
  for beverage in new_beverage:
    ManagerFactory.manager('beverage').create(beverage)

def get_beverages():
  beverages_return = []
  all_beverages = ManagerFactory.manager('beverage').get_all()
  beverages_num = random.randint(1, 10)
  selected_beverages = random.sample(all_beverages,beverages_num)
  for beverage in selected_beverages:
    modeled_beverage = Beverage(**beverage)
    if modeled_beverage not in beverages_return:
      beverages_return.append(modeled_beverage)
  return beverages_return