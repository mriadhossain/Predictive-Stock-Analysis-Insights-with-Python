
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the stock tickers and the date range
stock_tickers = ['MSFT', 'AAPL', 'NVDA', 'GOOGL', 'AMZN']
start_date = '2018-01-01'
end_date = '2023-12-31'

# Download stock data
data = yf.download(stock_tickers, start=start_date, end=end_date)['Adj Close']

# Calculate moving averages
moving_averages = {}  # To store moving average data separately
for ticker in stock_tickers:
    moving_averages[f'{ticker} 50d MA'] = data[ticker].rolling(window=50).mean()
    moving_averages[f'{ticker} 200d MA'] = data[ticker].rolling(window=200).mean()

# Plotting
plt.figure(figsize=(14, 7))
for ticker in stock_tickers:
    plt.plot(data.index, data[ticker], label=ticker)
    plt.plot(data.index, moving_averages[f'{ticker} 50d MA'], '--', label=f'{ticker} 50d MA')
    plt.plot(data.index, moving_averages[f'{ticker} 200d MA'], ':', label=f'{ticker} 200d MA')

plt.title('Stock Prices and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.show()
