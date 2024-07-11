from flask import Flask
from flask_cors import CORS
from apis.company_info import company_info_api

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Blueprints
app.register_blueprint(company_info_api)

if __name__ == '__main__':
    app.run(debug=True)