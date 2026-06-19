


import numpy as np
from x_returns import (xday_return_calc)

def cal_var_s(xdays_return):
  VAR_s = -np.percentile(xdays_return, 100 - (confidence*100)) * portf_value

  return VAR_s
