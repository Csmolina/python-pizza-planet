from flask import jsonify
import pytest
from app.controllers import ReportController

def test_report_controller(app, create_beverages, create_sizes, create_ingredients, create_orders):
  report, error = ReportController().generate_report()
  pytest.assume(error is None)
  for param, value in report.items():
    pytest.assume(report[param] == value)
