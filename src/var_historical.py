
import numpy as np


def cal_var_s(xdays_return, c, p_value):
  VAR_s = -np.percentile(xdays_return, 100 - (c*100)) * p_value

  return VAR_s
