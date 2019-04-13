import numpy as np

def s_mavg(dataset, window):
	"""
	initial implementation of simple moving average

	:param List dataset: dataset to compute
	:param Int window: moving average window
	:returns: an array of simple moving avgs
	:rtype: numpy.ndarray
	"""
	weigths = np.repeat(1.0, window)/window
	return np.convolve(dataset, weigths, 'valid')

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

def exp_mavg(dataset, window):
	"""
	initial implementation of exponential moving average

	:param List dataset: dataset to compute
	:param Int window: moving average window
	:returns: array of exponentially weighted moving avgs
	:rtype: numpy.ndarray
	"""
	weights = np.exp(np.linspace(-1., 0., window))
	weights /= weights.sum()
	a =  np.convolve(dataset, weights, mode='full')[:len(dataset)]
	a[:window] = a[window]
	return a
