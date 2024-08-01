
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock tickers and the date range
stock_tickers = ['MSFT', 'AAPL', 'NVDA', 'GOOGL', 'AMZN']
start_date = '2018-01-01'
end_date = '2023-12-31'

# Download stock data
data = yf.download(stock_tickers, start=start_date, end=end_date)['Adj Close']

# Calculate total return
total_return = ((data.iloc[-1] / data.iloc[0]) - 1) * 100

# Sort values for better visualization
total_return_sorted = total_return.sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
total_return_sorted.plot(kind='bar', color='Orange')
plt.title('Total Return (%) from 2018-01-01 to 2023-12-31')
plt.xlabel('Stock')
plt.ylabel('Total Return (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')

plt.show()



