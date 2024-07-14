from flask import jsonify, Blueprint, request
from common import get_fmp_data

statement_analysis_api = Blueprint('statement_analysis_api', __name__)

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
    endpoint = f'score/{symbol}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)

# returns enterprise values given a symbol
@statement_analysis_api.route('/enterprise-values/<symbol>', methods=['GET'])
def get_enterprise_values(symbol):
    endpoint = f'enterprise-values/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)