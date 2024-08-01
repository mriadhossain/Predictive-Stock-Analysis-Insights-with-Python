
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the stock tickers and the date range
stock_tickers = ['MSFT', 'AAPL', 'NVDA', 'GOOGL', 'AMZN']
start_date = '2018-01-01'
end_date = '2023-12-31'

# Download stock data
data = yf.download(stock_tickers, start=start_date, end=end_date)['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change()

# Calculate the correlation matrix
correlation_matrix = daily_returns.corr()

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.05)
plt.title('Correlation Matrix Heatmap')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()




