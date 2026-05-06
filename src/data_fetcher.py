import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker, start_date, end_date):
    """Fetches historical data from Yahoo Finance API."""
    print(f"--- Fetching data for {ticker} ---")
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError("No data found. Check the ticker symbol.")
        
        # Save raw data to data/ folder
        os.makedirs('data', exist_ok=True)
        data.to_csv(f'data/{ticker}_raw.csv')
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None