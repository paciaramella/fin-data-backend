from flask import jsonify, Blueprint, request
from common import get_fmp_data

price_targets_api = Blueprint('price_targets_api', __name__)

# returns price target consensus given a symbol
@price_targets_api.route('/price-target-consensus/<symbol>', methods=['GET'])
def get_price_target_consensus(symbol):
    endpoint = f'price-target-consensus/{symbol}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)