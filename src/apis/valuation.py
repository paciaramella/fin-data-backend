from flask import jsonify, Blueprint, request
from common import get_fmp_data

valuation_api = Blueprint('valuation_api', __name__)

def build_request(path, symbol, version):
    limit = request.args.get('limit')
    period = request.args.get('period')
    endpoint = f'{path}/{symbol}?limit={limit}&period={period}'
    data = get_fmp_data(endpoint, version)
    return data

# returns discounted cashflow given a symbol
@valuation_api.route('/discounted-cash-flow/<symbol>', methods=['GET'])
def get_discounted_cashflow(symbol):
    endpoint = f'discounted-cash-flow/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns levered cashflow given a symbol
@valuation_api.route('/advanced_levered_discounted-cash-flow/<symbol>', methods=['GET'])
def get_advanced_levered__discounted_cashflow(symbol):
    endpoint = f'advanced_levered_-cash-flow/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns company rating given a symbol
@valuation_api.route('/rating/<symbol>', methods=['GET'])
def get_rating(symbol):
    endpoint = f'rating/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns company rating given a symbol
@valuation_api.route('/historical-rating/<symbol>', methods=['GET'])
def get_historical_rating(symbol):
    endpoint = f'historical-rating/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)