import requests


api_key = 'DNSL6E10MUG8ZN2X'
base_url = 'https://www.alphavantage.co/query'

# Example: Get stock quotes for Apple Inc. (AAPL)
symbol = 'AAPL'
function = 'GLOBAL_QUOTE'
params = {'symbol': symbol, 'function': function, 'apikey': api_key}

response = requests.get(base_url, params=params)

# Check the requests (status code 200)
if response.status_code == 200:
    data = response.json()
    
    # Extracted and printed relevant information
    if 'Global Quote' in data:
        stock_data = data['Global Quote']
        print(f'Symbol: {stock_data["01. symbol"]}')
        print(f'Open: {stock_data["02. open"]}')
        print(f'High: {stock_data["03. high"]}')
        print(f'Low: {stock_data["04. low"]}')
        print(f'Price: {stock_data["05. price"]}')
        print(f'Volume: {stock_data["06. volume"]}')
        print(f'Latest Trading Day: {stock_data["07. latest trading day"]}')
        print(f'Previous Close: {stock_data["08. previous close"]}')
        print(f'Change: {stock_data["09. change"]}')
        print(f'Change Percent: {stock_data["10. change percent"]}')
else:
    print(f'Error: Failed to fetch data (Status code: {response.status_code})')