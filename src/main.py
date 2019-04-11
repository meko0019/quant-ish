#!/usr/bin/env python

import os
from binance.client import Client


try:
	api_key = os.environ.get(API_KEY)
	api_secret = os.environ.get(API_SECRET)
except Exception as e:
	return 

client = Client(api_key, api_secret)
