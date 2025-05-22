import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Read data from CSV file and remove commas from numeric values
def remove_commas_and_convert_to_float(s):
    return float(s.replace(',', ''))

dtype = {'Open': float, 'High': float, 'Low': float, 'Close': float, 'Volume': int}
converters = {'Open': remove_commas_and_convert_to_float, 'High': remove_commas_and_convert_to_float,
              'Low': remove_commas_and_convert_to_float, 'Close': remove_commas_and_convert_to_float,
              'Volume': remove_commas_and_convert_to_float}  # Corrected function name here

df = pd.read_csv('ril_stock_data.csv', dtype=dtype, converters=converters)
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
df.set_index('Date', inplace=True)  # Set 'Date' as the index

# Create a new column for daily price change
df['PriceChange'] = df['Close'] - df['Open']

# Plotting different types of graphs
plt.figure(figsize=(12, 8))

# Line chart of Closing Prices
plt.subplot(2, 2, 1)
plt.plot(df.index, df['Close'], marker='o')
plt.title('Closing Prices')

# Bar chart of Daily Price Changes
plt.subplot(2, 2, 2)
plt.bar(df.index, df['PriceChange'], color='green' if df['PriceChange'].mean() >= 0 else 'red')
plt.title('Daily Price Changes')

# Candlestick chart using Plotly
plt.subplot(2, 2, 3)
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
fig.update_layout(title='Candlestick Chart')
fig.show()

# Volume chart
plt.subplot(2, 2, 4)
plt.bar(df.index, df['Volume'], color='purple')
plt.title('Trading Volume')

plt.tight_layout()
plt.show()
