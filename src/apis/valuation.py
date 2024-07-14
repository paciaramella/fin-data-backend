from flask import jsonify, Blueprint, request
from constants import API_KEY, BASE_URL_v3, BASE_URL_v4
import requests

valuation_api = Blueprint('valuation_api', __name__)

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

def build_request(path, symbol, version):
    limit = request.args.get('limit')
    period = request.args.get('period')
    endpoint = f'{path}/{symbol}?limit={limit}&period={period}'
    data = get_fmp_data(endpoint, version)
    return data