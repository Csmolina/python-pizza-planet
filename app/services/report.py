from app.common.http_methods import GET
from flask import Blueprint, jsonify
from ..controllers import ReportController

report = Blueprint('report', __name__)
service = ReportController()
@report.route('/', methods=GET)
def get_report():
    entity, error = service.generate_report()
    response = entity if not error else {'error': error}
    status_code = 200 if entity else 404 if not error else 400
    return jsonify(response), status_code