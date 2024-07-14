from flask import jsonify, Blueprint, request
from common import get_fmp_data

financial_statement_api = Blueprint('financial_statement_api', __name__)

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