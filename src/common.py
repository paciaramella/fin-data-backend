from constants import API_KEY, BASE_URL_v3, BASE_URL_v4
import requests
# Helper function to make requests to the FMP API
def get_fmp_data(endpoint, version, params={}):
    base = BASE_URL_v3 if version == 3 else BASE_URL_v4
    params['apikey'] = API_KEY
    url = f"{base}/{endpoint}"
    response = requests.get(url, params=params)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error Response: {response.text}")
    return response.json()