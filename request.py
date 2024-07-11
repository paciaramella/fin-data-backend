import requests

API_KEY = 'Upd3bM4nObLXNuSZEJC7dRMdn3W9Tr2b'
BASE_URL = 'https://financialmodelingprep.com/api/v3'
symbol = 'AAPL'
endpoint = f'profile/{symbol}'
params = {'apikey': API_KEY}
url = f"{BASE_URL}/{endpoint}"
response = requests.get(url, params=params)

print(f"Request URL: {response.url}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")
