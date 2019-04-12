#!/usr/bin/env python

import os
import sys
sys.path.append(".")

from binance.client import Client
from binance.enums import *
from app.trends import mavg

try:
	api_key = os.environ.get('API_KEY')
	api_secret = os.environ.get('API_SECRET')
except Exception as e:
	raise e 

def main(tradepair):

	client = Client(api_key, api_secret)
	candles = client.get_klines(symbol=tradepair, interval=KLINE_INTERVAL_5MINUTE, limit=400)
	x_values = [float(i[4]) for i in candles]

	result = mavg.exp_mavg(x_values, 400)
	print(result)
	return result

if __name__ == "__main__":
	main('BTCUSDT')