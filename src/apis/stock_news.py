from flask import jsonify, Blueprint, request
from constants import API_KEY, BASE_URL_v3, BASE_URL_v4
import requests

stock_news_api = Blueprint('stock_news_api', __name__)

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