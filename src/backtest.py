import pandas as pd



def rolling_var_backtest(xday_retn, p_value, c):
    
    # ROLLING VAR
    xday_returns_rs = xday_retn * p_value

    var_rolling = (xday_retn.rolling(window=252, min_periods=252).quantile(1 - c).shift(1))
    var_rolling_rs = var_rolling * p_value

    backtest_df = pd.DataFrame({"Return": xday_returns_rs,
                                "VaR": var_rolling_rs})
    backtest_df= backtest_df.dropna()

    # Breach test
    backtest_df["Breach"] = (backtest_df["Return"] < backtest_df["VaR"]).astype(int)

    total_obs = len(backtest_df)
    breach = backtest_df["Breach"].sum()

    return backtest_df, total_obs, breach, 
