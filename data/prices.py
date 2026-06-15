import pandas as pd
import yfinance as yf
from ticker_list import tickers

def adj_close_price(tickers, start_date, end_date):
    adj_close_price = pd.DataFrame()

    for tick in tickers:
        data = yf.download(tick, start=start_date, end=end_date)

        if not data.empty:
            adj_close_price[tick] = data['Close']
        else:
            print("Data is unnavailable")

    print(adj_close_price)
    
    return adj_close_price