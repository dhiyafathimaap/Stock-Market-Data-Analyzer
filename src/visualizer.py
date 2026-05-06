import matplotlib.pyplot as plt
import seaborn as sns
import os

def save_plots(df, ticker):
    """Generates and saves stock analysis charts."""
    os.makedirs('outputs', exist_ok=True)
    plt.style.use('ggplot')
    
    # 1. Price & Moving Averages Chart
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.6)
    plt.plot(df['MA50'], label='50-Day MA', color='orange')
    plt.plot(df['MA200'], label='200-Day MA', color='red')
    plt.title(f'{ticker} Price Trend & Moving Averages')
    plt.legend()
    plt.savefig(f'outputs/{ticker}_trend.png')
    plt.close()

    # 2. Daily Returns Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Daily_Return'].dropna(), bins=50, kde=True, color='purple')
    plt.title(f'{ticker} Daily Returns Distribution')
    plt.savefig(f'outputs/{ticker}_returns.png')
    plt.close()
    
    print(f"--- Charts saved in outputs/ folder ---")