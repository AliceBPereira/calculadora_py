from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1
calculators_route_bp = Blueprint('calculators_routes', __name__)

@calculators_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    calc.calculate(request)
    
    return jsonify({"success": True}), 200