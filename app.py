from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key from FinancialModelingPrep
API_KEY = 'Upd3bM4nObLXNuSZEJC7dRMdn3W9Tr2b'
BASE_URL = 'https://financialmodelingprep.com/api/v3'


# Helper function to make requests to the FMP API
def get_fmp_data(endpoint, params={}):
    params['apikey'] = API_KEY
    url = f"{BASE_URL}/{endpoint}"
    print(f"Request URL: {url}")
    response = requests.get(url, params=params)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error Response: {response.text}")
    return response.json()
# returns important company information
@app.route('/company/profile/<symbol>', methods=['GET'])
def get_company_profile(symbol):
    endpoint = f'profile/{symbol}'
    data = get_fmp_data(endpoint)
    return jsonify(data)

# returns basic financials of a given company
@app.route('/company/financials/<symbol>', methods=['GET'])
def get_company_financials(symbol):
    endpoint = f'financials/income-statement/{symbol}'
    data = get_fmp_data(endpoint)
    return jsonify(data)

# returns stock of a given company
@app.route('/company/stock/<symbol>', methods=['GET'])
def get_company_stock(symbol):
    endpoint = f'quote/{symbol}'
    data = get_fmp_data(endpoint)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)