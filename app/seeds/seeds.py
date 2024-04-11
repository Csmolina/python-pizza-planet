import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..repositories.models import Ingredient, Size, Beverage
from ..settings import Config
from .utils import generators
from ..repositories.managers import ManagerFactory
from ..controllers.order import OrderController
from ..repositories.models import Ingredient,Beverage

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
create_session = sessionmaker(bind=engine)
session = create_session()

def add_sizes():
  new_sizes = generators.create_sizes()
  for size in new_sizes: 
    ManagerFactory.manager('size').create(size)
def add_beverages():
  new_beverage =  generators.create_beverages()
  for beverage in new_beverage:
    ManagerFactory.manager('beverage').create(beverage)

def add_ingredients():
  new_ingredient =  generators.create_ingredients()
  for ingredient in new_ingredient:
    ManagerFactory.manager('ingredient').create(ingredient)

def get_sizes():
  all_sizes = ManagerFactory.manager('size').get_all()
  size_index = random.randint(0, 4)
  return all_sizes[size_index]

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


def create_order():
  select_costumer = random.choice(generators.create_costumers())
  select_size = get_sizes()
  ingredients = get_ingredients();
  beverages = get_beverages(); 
  price = OrderController.calculate_order_price(select_size["price"],ingredients,beverages)
  new_order = {**select_costumer,
               "size_id":select_size["_id"],
               "date":generators.create_date(),
               "total_price":price
               }
  ManagerFactory.manager('order').create(new_order, ingredients, beverages)


def populate_database():
  add_sizes()
  add_ingredients()
  add_beverages()
  for _ in range(100):
    create_order()