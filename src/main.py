#!/usr/bin/env python

import os
from binance.client import Client
from binance.enums import *


try:
	api_key = os.environ.get('API_KEY')
	api_secret = os.environ.get('API_SECRET')
except Exception as e:
	raise e 

client = Client(api_key, api_secret)
result = client.get_klines(symbol='BTCUSDT', interval=KLINE_INTERVAL_5MINUTE, limit=400)
print(result)