
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.dates import date2num, num2date
from datetime import datetime

# Fetch historical stock price data for NVIDIA
ticker_symbol = 'NVDA'
data = yf.download(ticker_symbol, start='2018-01-01', end='2023-12-31')['Adj Close']

# Prepare the data
data = pd.DataFrame(data)
data['Date'] = data.index
data['Date'] = data['Date'].apply(date2num)
data['Days'] = (data['Date'] - data['Date'].min())

# Independent variable
X = data[['Days']]
# Dependent variable
y = data['Adj Close']

# Creating the model
model = LinearRegression()

# Training the model with all data
model.fit(X, y)

# Predicting the stock price at the end of 2026
# Calculate days from the start to 2026-12-31
end_date = date2num(datetime(2026, 12, 31))
days_from_start_to_end = end_date - data['Date'].min()
# Predicting
predicted_price = model.predict([[days_from_start_to_end]])

print(f"Predicted NVDA stock price at the end of 2026: ${predicted_price[0]:.2f}")

# Making predictions for plotting
predictions = model.predict(X)

# Plotting
plt.figure(figsize=(14, 7))
plt.scatter(data.index, y, color='skyblue', label='Actual Price')
plt.plot(data.index, predictions, color='red', linewidth=2, label='Linear Regression')

# Highlight the prediction point
plt.scatter(num2date(end_date), predicted_price, color='green', marker='*', s=100, label='End of 2026 Prediction')

plt.title('NVDA Stock Price Prediction Using Linear Regression')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
