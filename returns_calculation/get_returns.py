import pandas as pd
import yfinance as yf
import datetime as dt

# Get the tickers
file_path = 'returns_calculation/tickers.xlsx' 
df = pd.read_excel(file_path)
yf_tickers = df['yf Ticker'].tolist()

# Getting the data from 2020
data = yf.download(tickers=" ".join(yf_tickers), start="2020-01-01", end=dt.datetime.now())
close_prices = data['Adj Close']

# Calculate daily returns
returns_df = close_prices.pct_change()

# Transform the dataframe
returns_final = returns_df.reset_index().melt(id_vars='Date', var_name='Ticker', value_name='Return')
returns_final = returns_final.dropna()

print(returns_final)
# Write it out to csv
returns_final.to_csv('returns.csv', index=False)
print("Written out to 'results.csv'")