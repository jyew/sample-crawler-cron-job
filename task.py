import requests
from datetime import datetime

def get_bitcoin_price():
    api_link = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(api_link)
    print(response.json())

if __name__ == "__main__":
    print(f"Running script at {datetime.now()}")
    get_bitcoin_price()