from src.data_fetcher import fetch_stock_data
from src.processor import process_data
from src.visualizer import save_plots

def run_analyzer():
    print("==========================================")
    print("   STOCK MARKET DATA ANALYSER (v1.0)     ")
    print("==========================================")
    
    # 1. User Input
    symbol = input("Enter Ticker Symbol (e.g., AAPL, TSLA, MSFT): ").upper()
    start_date = "2023-01-01"
    end_date = "2024-01-01"
    
    # 2. Fetch Data
    raw_data = fetch_stock_data(symbol, start_date, end_date)
    
    if raw_data is not None:
        # 3. Process Data
        # 'processed_data' holds the table, 'vol' holds the risk number
        processed_data, vol = process_data(raw_data)
        
        # 4. Generate Visuals
        save_plots(processed_data, symbol)
        
        # 5. Extract Final Metrics
        # .item() converts the single-value Series into a float for printing
        latest_price = processed_data['Close'].iloc[-1].item()
        
        # 6. Final Terminal Report
        print("\n" + "="*30)
        print(f"📊 ANALYSIS COMPLETE: {symbol}")
        print("="*30)
        print(f"💰 Latest Close Price: ${latest_price:.2f}")
        print(f"📉 Annual Volatility:  {vol:.2%}")
        print(f"📂 Data Saved to:      data/{symbol}_raw.csv")
        print(f"🖼️ Charts Saved to:    outputs/")
        print("="*30 + "\n")
    else:
        print("❌ Failed to retrieve data. Please check the ticker and internet connection.")

if __name__ == "__main__":
    run_analyzer()