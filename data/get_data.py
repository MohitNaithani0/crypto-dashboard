# data/get_data.py

import requests
import pandas as pd
from datetime import datetime

def fetch_btc_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30",  # past 30 days
        "interval": "daily"
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])

    # Convert timestamp to datetime
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['date', 'price']]
    return df

if __name__ == "__main__":
    df = fetch_btc_data()
    print(df.head())
    df.to_csv("data/btc_price_30d.csv", index=False)
