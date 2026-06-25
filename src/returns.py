
import numpy as np


def cal_logs(adj_close_price):
  log_returns = np.log(adj_close_price/adj_close_price.shift(1))
  log_returns = log_returns.dropna()

  return log_returns



