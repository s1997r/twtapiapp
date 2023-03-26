from flask import Flask ,jsonify
from urllib.parse import quote
import pandas as pd
app = Flask(__name__)


@app.route('/<string:category>/<string:time>')
def get_data(category, time):
    time = quote(time)
    # Load data from CSV file into Pandas DataFrame
    sheet_id = "1rSzgHtvNEB17B0hoP65QiH15qOw_Cu_4vvyijWSkTCU"
    sheet_name = time
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    # Filter data based on input parameters
    filtered_df = df[(df['location_name'] == category)]
    # Convert filtered data to JSON format and return as a response
    data = jsonify(filtered_df.to_dict(orient='records'))}
    return {"data": data}

if __name__ == "__main__":
    app.run()
