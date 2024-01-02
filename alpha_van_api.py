import requests
import pandas as pd

from secrets import key

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={key}'
r = requests.get(url)
data = r.json()

# print(data)
print(f"Status Code: {r.status_code}")
print(data.keys())

# print(f"metadata: {data['metadata']}")

# print(f"Top gainers: {data['top_gainers']}")

top_gainers = data['top_gainers']

keys = []

for ticker in top_gainers:
    keys.append(ticker['ticker'])
    
print(keys)

key_price_dict = {}

for ticker in top_gainers:
    key_price_dict[ticker['ticker']] = ticker['price']

print(key_price_dict)


dataframe = pd.DataFrame(top_gainers)

print(dataframe)

