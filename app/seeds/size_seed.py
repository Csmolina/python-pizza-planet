from app.repositories.managers import ManagerFactory
import random
from .utils import generators

def add_sizes():
  new_sizes = generators.create_sizes()
  for size in new_sizes: 
    ManagerFactory.manager('size').create(size)

def get_sizes():
  all_sizes = ManagerFactory.manager('size').get_all()
  size_index = random.randint(0, 4)
  return all_sizes[size_index]