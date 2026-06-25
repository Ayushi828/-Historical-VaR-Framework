

def get_hist_returns(log_returns, wt):
  historical_returns = (log_returns * wt).sum(axis=1)
  
  return historical_returns
