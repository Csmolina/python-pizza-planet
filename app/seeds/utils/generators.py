from datetime import datetime 
from faker import Faker

fake = Faker()

def create_costumers()->list:
  costumers=[]  
  for _ in range(20):
    costumer={
      "client_name":fake.name(),
      "client_dni":str(fake.random_number(digits=10)),
      "client_address":fake.address(),
      "client_phone":fake.phone_number()
    }
    costumers.append(costumer)
  return costumers

def create_sizes() -> list:
    sizes = [
        {"name": "Small", "price": 5.00},
        {"name": "Medium", "price": 8.00},
        {"name": "Large", "price": 11.00},
        {"name": "X-Large", "price": 14.00},
        {"name": "Gigantic", "price": 17.00}
    ]
    return sizes

def create_ingredients() -> list:
    ingredients = [
        {"name": "Pepperoni", "price": 3.50},
        {"name": "Mozzarella cheese", "price": 2.75},
        {"name": "Tomato sauce", "price": 1.25},
        {"name": "Mushrooms", "price": 1.90},
        {"name": "Ham", "price": 4.25},
        {"name": "Bell peppers", "price": 2.10},
        {"name": "Onions", "price": 1.50},
        {"name": "Olives", "price": 1.75},
        {"name": "Italian sausage", "price": 3.80},
        {"name": "Jalapeño peppers", "price": 2.30}
    ]
    return ingredients

def create_beverages() -> list:
    beverages = [
        {"name": "Water", "price": 1.50},
        {"name": "Coffee", "price": 1.75},
        {"name": "Tea", "price": 2.00},
        {"name": "Orange juice", "price": 2.25},
        {"name": "Lemonade", "price": 2.50},
        {"name": "Cola", "price": 2.75},
        {"name": "Iced tea", "price": 3.00},
        {"name": "Milk", "price": 3.00},
        {"name": "Hot chocolate", "price": 2.50},
        {"name": "Apple juice", "price": 2.25}
    ]
    return beverages

def create_date() -> str:
  start_date = datetime(2020, 1, 1)
  end_date = datetime(2024, 12, 31)
  random_datetime = fake.date_time_between(start_date=start_date, end_date=end_date)
  return random_datetime