from flask import jsonify, Blueprint, request
from common import get_fmp_data

quote_api = Blueprint('quote_api', __name__)

# returns just the price and volume for a stock
@quote_api.route('/quote-short/<symbol>', methods=['GET'])
def get_live_price(symbol):
    endpoint = f'quote-short/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)