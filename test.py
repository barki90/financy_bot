from datetime import datetime
import time

import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()


API_KEY = os.getenv('APIKEY')
URL = f"https://api.finage.co.uk/last/trade/stock/TSLA?apikey={API_KEY}"

response = requests.get(URL)

t = response.json()
print(t)
# time
time_stamp = t['timestamp'] / 1000
my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))

price = t['price']

print(price, '$', sep='')
