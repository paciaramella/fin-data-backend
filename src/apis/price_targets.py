from flask import jsonify, Blueprint, request
from constants import API_KEY, BASE_URL_v3, BASE_URL_v4
import requests

price_targets_api = Blueprint('price_targets_api', __name__)

# Helper function to make requests to the FMP API
def get_fmp_data(endpoint, version, params={}):
    base = BASE_URL_v3 if version == 3 else BASE_URL_v4
    params['apikey'] = API_KEY
    url = f"{base}/{endpoint}"
    print(f"Request URL: {url}")
    response = requests.get(url, params=params)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error Response: {response.text}")
    return response.json()

# returns price target consensus given a symbol
@price_targets_api.route('/price-target-consensus/<symbol>', methods=['GET'])
def get_price_target_consensus(symbol):
    endpoint = f'price-target-consensus/{symbol}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)