from his_returns import (get_hist_returns)

def xday_return_calc(historical_returns):
  xdays_return = historical_returns.rolling(window = days).sum()
  xdays_return = xdays_return.dropna()
  return xdays_return
  
