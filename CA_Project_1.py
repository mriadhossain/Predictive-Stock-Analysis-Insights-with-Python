import yfinance as yf

# Define the stock tickers for Microsoft, Apple, NVIDIA, Alphabet (Google), and Amazon
stock_tickers = ['MSFT', 'AAPL', 'NVDA', 'GOOGL', 'AMZN']

# Define the start and end dates for fetching the data
start_date = '2018-01-01'  # Example start date
end_date = '2023-12-31'    # Example end date

def fetch_and_display_stock_data(tickers, start, end):
    for ticker in tickers:
        # Fetch the stock data
        stock_data = yf.download(ticker, start=start, end=end)
        
        # Display the first and last 5 rows of the data
        print(f"First 5 rows for {ticker}:")
        print(stock_data.head())
        print("\nLast 5 rows for {ticker}:")
        print(stock_data.tail())
        print("-" * 50)  # Separator for clarity

# Run the function with the specified parameters
fetch_and_display_stock_data(stock_tickers, start_date, end_date)
