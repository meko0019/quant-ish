import sys
sys.path.append("..")

import numpy as np
import pytest
from app.trends import mavg


@pytest.mark.parametrize("test_input,expected", [((np.linspace(1.0, 10, 10), 2), [1] + list(np.linspace(1.5, 9.5, 9)))])
def test_s_mavg(test_input, expected):
	assert len(mavg.s_mavg(*test_input)) + (test_input[1] - 1) == len(expected)
	assert list(mavg.s_mavg(*test_input)) == expected[test_input[1]-1:len(expected)]
	#TODO: improve this, only works for window of 2


@pytest.mark.parametrize("test_input,expected", [((np.linspace(1.0, 10, 10), 2), [1] + list(np.linspace(1.5, 9.5, 9)))])
def test_w_mavg(test_input, expected):
	pass

def exp_mavg():
	pass


