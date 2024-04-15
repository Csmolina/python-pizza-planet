from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .beverage_seed import add_beverages
from .ingredient_seed import add_ingredients
from .order_seed import create_order
from .size_seed import add_sizes
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
    for _ in range(100):
      create_order(costumer_list)
  except:
    raise("An error occurred when trying to populate the database.")    