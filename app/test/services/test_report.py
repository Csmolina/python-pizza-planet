import pytest

def test_get_report_service(client, report_uri, create_order):
  response = client.get(report_uri)
  report_data = response.json
  pytest.assume(response.status.startswith("200")) 
  pytest.assume(report_data["top_ingredient"])
  pytest.assume(report_data["top_month"])
  pytest.assume(report_data["top_three_clients"])
