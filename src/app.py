from flask import Flask
from flask_cors import CORS
from apis.company_info import company_info_api
from apis.financial_statements import financial_statement_api
from apis.statement_analysis import statement_analysis_api
from apis.valuation import valuation_api
from apis.price_targets import price_targets_api
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Blueprints
app.register_blueprint(company_info_api)
app.register_blueprint(financial_statement_api)
app.register_blueprint(statement_analysis_api)
app.register_blueprint(valuation_api)
app.register_blueprint(price_targets_api)

if __name__ == '__main__':
    app.run(debug=True)