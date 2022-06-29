from pprint import pprint
import requests
import sys
import logging
import pprint
from datetime import datetime

print('Executing task.py')

log = logging.getLogger("my-logger")

def get_bitcoin_price():
    api_link = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(api_link)
    pprint.pprint(response.json())

if __name__ == "__main__":
    print(f"Running script at {datetime.now()}", flush=True)
    get_bitcoin_price()
    log.info("Hello, world")
    sys.stdout.flush()