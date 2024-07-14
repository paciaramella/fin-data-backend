from flask import jsonify, Blueprint, request
from common import get_fmp_data

company_info_api = Blueprint('company_info_api', __name__)
    
# returns important company information
@company_info_api.route('/company/profile/<symbol>', methods=['GET'])
def get_company_profile(symbol):
    endpoint = f'profile/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns stock of a given company
@company_info_api.route('/company/stock/<symbol>', methods=['GET'])
def get_company_stock(symbol):
    endpoint = f'quote/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns key executives of a given company
@company_info_api.route('/company/key_executives/<symbol>', methods=['GET'])
def get_key_executives(symbol):
    endpoint = f'/key_executives?symbol={symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns executive compensation of a given company
@company_info_api.route('/company/governance/executive_compensation/<symbol>', methods=['GET'])
def get_executive_profile(symbol):
    endpoint = f'/governance/executive_compensation?symbol={symbol}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)

# returns executive comp benchmark of a given company
@company_info_api.route('/company/executive-compensation-benchmark/<year>', methods=['GET'])
def get_executive_comp_benchmark(year):
    endpoint = f'/executive-compensation-benchmark?year={year}'
    data = get_fmp_data(endpoint, 4)
    return jsonify(data)

# returns company market cap
@company_info_api.route('/company/market-capitalization/<symbol>', methods=['GET'])
def get_company_market_cap(symbol):
    endpoint = f'/market-capitalization/{symbol}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns HISTORICAL company market cap
@company_info_api.route('/company/historical-market-capitalization/<symbol>', methods=['GET'])
def get_historical_company_market_cap(symbol):
    limit = request.args.get('limit')
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    endpoint = f'/historical-market-capitalization/{symbol}?limit={limit}&from={from_date}&to={to_date}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns stock grade of a company
@company_info_api.route('/company/grade/<symbol>', methods=['GET'])
def get_company_grade(symbol):
    limit = request.args.get('limit')
    endpoint = f'/grade/{symbol}?limit={limit}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns analyst estimates of a company
@company_info_api.route('/company/analyst-estimates/<symbol>', methods=['GET'])
def get_company_analyst_estimates(symbol):
    period = request.args.get('period')
    limit = request.args.get('limit')
    endpoint = f'/analyst-estimates/{symbol}?period={period}&limit={limit}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)
