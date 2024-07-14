from flask import jsonify, Blueprint, request
from constants import API_KEY, BASE_URL_v3, BASE_URL_v4
import requests

statement_analysis_api = Blueprint('statement_analysis_api', __name__)

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


# returns key metrics given a symbol
@statement_analysis_api.route('/key-metrics/<symbol>', methods=['GET'])
def get_key_metrics(symbol):
    data = build_request('key-metrics', symbol, 3)
    return jsonify(data)

# returns important ratios given a symbol
@statement_analysis_api.route('/ratios/<symbol>', methods=['GET'])
def get_ratios(symbol):
    data = build_request('ratios', symbol, 3)
    return jsonify(data)

# returns cash flow growth given a symbol
@statement_analysis_api.route('/cash-flow-statement-growth/<symbol>', methods=['GET'])
def get_cash_flow_statement_growth(symbol):
    data = build_request('cash-flow-statement-growth', symbol, 3)
    return jsonify(data)

# returns income growth given a symbol
@statement_analysis_api.route('/income-statement-growth/<symbol>', methods=['GET'])
def get_income_statement_growth(symbol):
    data = build_request('income-statement-growth', symbol, 3)
    return jsonify(data)

# returns balance sheet growth given a symbol
@statement_analysis_api.route('/balance-sheet-statement-growth/<symbol>', methods=['GET'])
def get_balance_sheet_statement_growth(symbol):
    data = build_request('balance-sheet-statement-growth', symbol, 3)
    return jsonify(data)

# returns financial growth given a symbol
@statement_analysis_api.route('/financial-growth/<symbol>', methods=['GET'])
def get_financial_growth(symbol):
    data = build_request('financial-statement-growth', symbol, 3)
    return jsonify(data)

# returns financial score given a symbol
@statement_analysis_api.route('/score/<symbol>', methods=['GET'])
def get_financial_score(symbol):
    data = build_request('score', symbol, 4)
    return jsonify(data)

# returns enterprise values given a symbol
@statement_analysis_api.route('/enterprise-values/<symbol>', methods=['GET'])
def get_enterprise_values(symbol):
    data = build_request('enterprise-values', symbol, 3)
    return jsonify(data)