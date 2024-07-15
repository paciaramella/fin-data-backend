from flask import jsonify, Blueprint, request
from common import get_fmp_data

earnings_api = Blueprint('earnings_api', __name__)

# returns A list of upcoming & past earnings announcements for publicly traded companies, including the date, estimated earnings per share (EPS), and actual EPS (if available).
@earnings_api.route('/earning_calendar/', methods=['GET'])
def get_earnings_calendar():
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    endpoint = f'earning_calendar?from={from_date}&to={to_date}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)

# returns A list of historical & upcoming earnings announcements for a specific company, including the date, estimated EPS, and actual EPS.
@earnings_api.route('/historical/earning_calendar/<symbol>', methods=['GET'])
def get_historical_earnings_calendar(symbol):
    limit = request.args.get('limit')
    endpoint = f'historical/earning_calendar/{symbol}?limit={limit}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)