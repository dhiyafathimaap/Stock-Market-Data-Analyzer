import pandas as pd
import numpy as np

def process_data(df):
    """Cleans data and calculates financial metrics."""
    # Handle missing values
    df = df.ffill()
    
    # Calculate Moving Averages
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    
    # Calculate Daily Returns
    df['Daily_Return'] = df['Close'].pct_change()
    
    # Calculate Volatility (Annualized)
    volatility = df['Daily_Return'].std() * np.sqrt(252)
    
    return df, volatility