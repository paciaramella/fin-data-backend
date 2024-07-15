from flask import jsonify, Blueprint, request
from common import get_fmp_data

stock_news_api = Blueprint('stock_news_api', __name__)

# returns price target consensus given a symbol
@stock_news_api.route('/stock_news/', methods=['GET'])
def get_stock_news():
    page = request.args.get('page')
    tickers = request.args.get('tickers')
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    limit = request.args.get('limit')
    endpoint = f'stock_news?tickers={tickers}&page={page}&from={from_date}&to={to_date}&limit={limit}'
    data = get_fmp_data(endpoint, 3)
    return jsonify(data)