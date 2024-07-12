from flask import jsonify, Blueprint, request
from constants import API_KEY, BASE_URL_v3, BASE_URL_v4
import requests

financial_statement_api = Blueprint('financial_statement_api', __name__)

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

# returns income statements given a cik or symbol
@financial_statement_api.route('/income-statement/<id>', methods=['GET'])
def get_income_statements(id):
    limit = request.args.get('limit')
    period = request.args.get('period')
    datatype = request.args.get('datatype')
    endpoint = f'income-statement/{id}?limit={limit}&period={period}&datatype={datatype}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns balance sheet statements given a cik or symbol
@financial_statement_api.route('/balance-sheet-statement/<id>', methods=['GET'])
def get_balance_sheet_statements(id):
    limit = request.args.get('limit')
    period = request.args.get('period')
    datatype = request.args.get('datatype')
    endpoint = f'balance-sheet-statement/{id}?limit={limit}&period={period}&datatype={datatype}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns cash flow sheet statements given a cik or symbol
@financial_statement_api.route('/cash-flow-statement/<id>', methods=['GET'])
def get_cash_flow_statements(id):
    limit = request.args.get('limit')
    period = request.args.get('period')
    datatype = request.args.get('datatype')
    endpoint = f'cash-flow-statement/{id}?limit={limit}&period={period}&datatype={datatype}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)