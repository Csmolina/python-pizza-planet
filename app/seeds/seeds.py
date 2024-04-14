from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .beverage_seed import add_beverages, get_beverages
from .ingredient_seed import add_ingredients, get_ingredients
from .order_seed import create_order
from .size_seed import add_sizes, get_sizes
from ..settings import Config
from .utils import generators


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
create_session = sessionmaker(bind=engine)
session = create_session()

def populate_database():
  try:
    add_sizes()
    add_ingredients()
    add_beverages()
    costumer_list = generators.create_costumers()
    sizes = get_sizes()
    ingredients = get_ingredients()
    beverages = get_beverages()
    for _ in range(100):
      create_order(costumer_list,sizes, ingredients, beverages)
  except:
    raise("An error occurred when trying to populate the database.")    