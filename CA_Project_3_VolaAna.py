
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

# Calculate daily returns
daily_returns = data.pct_change()

# Calculate annualized volatility
annualized_volatility = daily_returns.std() * np.sqrt(252)

# Sort values for a more intuitive graph
annualized_volatility_sorted = annualized_volatility.sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
annualized_volatility_sorted.plot(kind='bar', color='pink')
plt.title('Annualized Volatility from 2018-01-01 to 2023-12-31')
plt.xlabel('Stock')
plt.ylabel('Annualized Volatility')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')

plt.show()

