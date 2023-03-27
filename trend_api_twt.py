from flask import Flask ,jsonify
from urllib.parse import quote
import pandas as pd
app = Flask(__name__)



def get_data(category, time):
    time = quote(time)
    # Load data from CSV file into Pandas DataFrame
    sheet_id = "1rSzgHtvNEB17B0hoP65QiH15qOw_Cu_4vvyijWSkTCU"
    sheet_name = time
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    # Filter data based on input parameters
    filtered_df = df[(df['location_name'] == category)]
    data_list=[]
    for index, row in filtered_df.iterrows():
        tmp_data = {"trend_name":row['trend_name'],"trend_url":row['trend_url'],"trend_volume":row['tweet_volume']}
        data_list.append(tmp_data)
    #final_data = {"data":data_list}
    # Convert filtered data to JSON format and return as a response
    #data = filtered_df.to_dict(orient='records')
    final_data = {"data": data}
    return final_data

@app.route('/<string:category>/<string:time>')
def get_trend_details(category, time):
    twitter_trend_data=get_data(category, time)
    return jsonify(twitter_trend_data)

if __name__ == "__main__":
    app.run()
