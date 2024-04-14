import random
from app.controllers.order import OrderController
from app.repositories.managers import ManagerFactory
from .utils import generators

def create_order(costumer_list, sizes, ingredients, beverages):
  select_costumer = random.choice(costumer_list)
  select_size = sizes
  select_ingredients = ingredients
  select_beverages = beverages 
  price = OrderController.calculate_order_price(select_size["price"],select_ingredients,select_beverages)
  new_order = {**select_costumer,
               "size_id":select_size["_id"],
               "date":generators.create_date(),
               "total_price":price
               }
  ManagerFactory.manager('order').create(new_order, select_ingredients, select_beverages)