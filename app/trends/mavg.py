import pandas as pd 

def s_mavg(dataset, i, n):
	"""
	initial implementation of simple moving average

	:param List dataset: dataset to compute
	:param Int i: index of interest in the dataset
	:param Int n: number of data points
	:returns: simple moving avg value at time i 
	:rtype: float
	"""

	if i < n-1:
		return 0
	else:
		return (sum(dataset[(i-n+1):(i+1)])/n)

def w_mavg(dataset, i, n):
	"""
	initial implementation of weighted moving average

	:param List dataset: dataset to compute
	:param Int i: index of interest in the dataset
	:param Int n: number of data points
	:returns: weighted moving avg value at time i 
	:rtype: float
	"""

	if i < n-1:
		return 0
	else:
		return (sum(dataset[(i-n+1):(i+1)])/n)

def exp_mavg(dataset, n):
	"""
	initial implementation of exponential moving average

	:param List dataset: dataset to compute
	:param Int i: index of interest in the dataset
	:param Int n: number of data points
	:returns: exponential moving avg value at time i 
	:rtype: float
	"""
	return pd.ewma(dataset, com=(n-1)/2)