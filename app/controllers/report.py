from datetime import datetime
from flask import jsonify
from .order import OrderController
from collections import Counter
from sqlalchemy.exc import SQLAlchemyError
class ReportController:

  def get_orders(self):
    orders = OrderController.get_all()
    return orders

  def get_ingredients_names(self,orders):
    ingredients_names = []
    for order in orders:
      for detail_row in order["detail"]:
        if detail_row["ingredient"]:
          ingredients_names.append(detail_row["ingredient"]["name"])
    return ingredients_names

  def get_months(self,orders):
    months = []
    for order in orders:
      month = datetime.strptime(order["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%B")
      months.append(month)
    return months

  def get_client_names(self,orders):
    clients_names = []
    for order in orders:
      clients_names.append(order["client_name"])
    return clients_names
  
  def most_requested_item(self,items):
    item_counter = Counter(items)
    top_item = max(item_counter, key = item_counter.get)
    return top_item
  
  def top_three_clients(self,clients):
    client_counter = Counter(clients)
    top_three_clients = client_counter.most_common(3)
    top_three_clients_names = [client[0] for client in top_three_clients]
    return top_three_clients_names

  def generate_report(self):
    try:
      orders = jsonify(self.get_orders()).json[0]
      ingredients = self.get_ingredients_names(orders)
      months = self.get_months(orders)
      clients = self.get_client_names(orders)
      top_ingredient = self.most_requested_item(ingredients)
      top_month = self.most_requested_item(months)
      top_three_clients = self.top_three_clients(clients)

      return {
        "top_ingredient": top_ingredient,
        "top_month": top_month,
        "top_three_clients": top_three_clients
      },None
  
    except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)