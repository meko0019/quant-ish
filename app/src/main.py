#!/usr/bin/env python

import os
import sys
sys.path.append(".")

from binance.client import Client
from binance.enums import *
from app.trends import mavg
import matplotlib.pyplot as plt

try:
	api_key = os.environ.get('API_KEY')
	api_secret = os.environ.get('API_SECRET')
except Exception as e:
	raise e 

def main(tradepair):

	client = Client(api_key, api_secret)
	candles = client.get_klines(symbol=tradepair, interval=KLINE_INTERVAL_5MINUTE, limit=400)
	x_values = [float(i[4]) for i in candles]

	result = mavg.exp_mavg(x_values, 20)
	result_ = mavg.s_mavg(x_values, 20)
	plt.plot(x_values, label = 'BTC')
	plt.plot(result, label = 'EXPMAVG')
	plt.plot(result_, label = 'SMAVG')
	plt.legend()
	plt.show()

if __name__ == "__main__":
	main('BTCUSDT')