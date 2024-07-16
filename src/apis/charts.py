from flask import jsonify, Blueprint, request
from common import get_fmp_data

chart_api = Blueprint('chart_api', __name__)

# returns chart for historical data given a stock
@chart_api.route('/historical-price-full/<symbol>')
def get_stock_chart(symbol):
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    serietype = request.args.get('serietype')
    endpoint = f'/historical-price-full/{symbol}?to={to_date}&from={from_date}&serietype={serietype}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)