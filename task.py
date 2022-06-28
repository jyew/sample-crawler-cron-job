import requests
import sys
from datetime import datetime

def get_bitcoin_price():
    api_link = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(api_link)
    print(response.json(), flush=True)

if __name__ == "__main__":
    print(f"Running script at {datetime.now()}", flush=True)
    get_bitcoin_price()
    sys.stdout.flush()