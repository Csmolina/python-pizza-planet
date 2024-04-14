import random
from app.controllers.order import OrderController
from app.repositories.managers import ManagerFactory
from .beverage_seed import get_beverages
from .ingredient_seed import get_ingredients
from .size_seed import get_sizes
from .utils import generators

def create_order(costumer_list):
  sizes = get_sizes()
  ingredients = get_ingredients()
  beverages = get_beverages()
  select_costumer = random.choice(costumer_list)
  price = OrderController.calculate_order_price(sizes["price"],ingredients,beverages)
  new_order = {**select_costumer,
               "size_id":sizes["_id"],
               "date":generators.create_date(),
               "total_price":price
               }
  ManagerFactory.manager('order').create(new_order, ingredients, beverages)