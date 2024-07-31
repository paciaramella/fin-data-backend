from flask import Blueprint

data_extraction_api = Blueprint('data_extraction_api', __name__)

@data_extraction_api.route('/extract-data/<data>', methods=['GET'])
def extract_data(data):
    import pandas as pd
    # Convert JSON to DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to Excel
    excel_file = "sbux_key_metrics_2024.xlsx"
    df.to_excel(excel_file, index=False)

    return "Data successfully written to {excel_file}"
