from returns import (logs)


def get_hist_returns(log_returns, wt):
  historical_returns = (log_returns * wt).sum(axis=1)
  
  return historical_returns

  print("\n","-"*10, "\t HISTORICAL RETURNS\t", "-"*10)
  print(historical_returns)
