from flask import jsonify, Blueprint
import requests

API_KEY = 'Upd3bM4nObLXNuSZEJC7dRMdn3W9Tr2b'
BASE_URL_v3 = 'https://financialmodelingprep.com/api/v3'
BASE_URL_v4 = 'https://financialmodelingprep.com/api/v4'

company_info_api = Blueprint('company_info_api', __name__)

# Helper function to make requests to the FMP API
def get_fmp_data(endpoint, version, params={}):
    base = BASE_URL_v3 if version == 3 else BASE_URL_v4
    print(f"APIKEY: {API_KEY}")
    params['apikey'] = API_KEY
    url = f"{base}/{endpoint}"
    print(f"Request URL: {url}")
    response = requests.get(url, params=params)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error Response: {response.text}")
    return response.json()
# returns important company information
@company_info_api.route('/company/profile/<symbol>', methods=['GET'])
def get_company_profile(symbol):
    endpoint = f'profile/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns basic financials of a given company
@company_info_api.route('/company/financials/<symbol>', methods=['GET'])
def get_company_financials(symbol):
    endpoint = f'financials/income-statement/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns stock of a given company
@company_info_api.route('/company/stock/<symbol>', methods=['GET'])
def get_company_stock(symbol):
    endpoint = f'quote/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns executive compensation of a given company
@company_info_api.route('/governance/executive_compensation/<symbol>', methods=['GET'])
def get_executive_profile(symbol):
    endpoint = f'/governance/executive_compensation?symbol={symbol}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)

# returns executive comp benchmark of a given company
@company_info_api.route('/executive-compensation-benchmark/<year>', methods=['GET'])
def get_executive_comp_benchmark(year):
    endpoint = f'/executive-compensation-benchmark?year={year}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)
