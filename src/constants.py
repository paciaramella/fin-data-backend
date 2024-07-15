import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()
# Access the API key from the environment variables
API_KEY = os.getenv('API_KEY')
BASE_URL_v3 = 'https://financialmodelingprep.com/api/v3'
BASE_URL_v4 = 'https://financialmodelingprep.com/api/v4'
