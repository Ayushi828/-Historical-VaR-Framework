import datetime as dt

def time_range(years):
  end_date = dt.datetime.now()
  start_date = end_date - dt.timedelta(days = 365 * years)
  print(f"The time range for data is {start_date.date()} to {end_date.date()}")
