from flask import Flask
from apis.company_info import company_info_api

app = Flask(__name__)

# Blueprints
app.register_blueprint(company_info_api)

if __name__ == '__main__':
    app.run(debug=True)