from flask import Flask, render_template
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_airline_data():
    # Example using CSV as placeholder
    df = pd.read_csv('data/sample_airline_data.csv')
    return df

def process_data(df):
    popular_routes = df['Route'].value_counts().head(5).to_dict()
    price_trend = df.groupby('Date')['Price'].mean().reset_index().to_dict(orient='list')
    demand_by_location = df['Destination'].value_counts().to_dict()
    return popular_routes, price_trend, demand_by_location

@app.route('/')
def dashboard():
    df = fetch_airline_data()
    routes, price_trend, demand = process_data(df)
    return render_template('dashboard.html',
                           routes=routes,
                           price_dates=price_trend['Date'],
                           price_values=price_trend['Price'],
                           demand=demand)

if __name__ == '__main__':
    app.run(debug=True)
