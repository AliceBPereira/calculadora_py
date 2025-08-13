from flask import Blueprint, jsonify, request

calculators_route_bp = Blueprint('calculators_routes', __name__)

@calculators_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    print(request.json)
    return jsonify({"success": True}), 200