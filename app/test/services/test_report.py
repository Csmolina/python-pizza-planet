import pytest

def test_get_report_service(client, report_uri, create_order):
  response = client.get(report_uri)
  report_data = response.json
  assert response.status.startswith("200")
  assert report_data["top_ingredient"]
  assert report_data["top_month"]
  assert report_data["top_three_clients"]
