from datetime import datetime
import MetaTrader5 as mt
import pandas as pd
import pytz

USER_ACC = 0000000000   # your account number
SERVER = ''             # your broker's server
USER_PASS = ''          # your account password

mt.initialize(
    login=USER_ACC,
    server=SERVER,
    password=USER_PASS,
)

login = mt.login(USER_PASS, USER_PASS, SERVER)
account_info = mt.account_info()
print(account_info)

login_number = account_info.login
balance = account_info.balance
equity = account_info.equity
print()
print('Login:', login_number)
print('Balance: ', balance)
print('Equity: ', equity)

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt.__author__)
print("MetaTrader5 package version: ", mt.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form

pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display
# import pytz module for working with time zone

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2023, 8, 1, tzinfo=timezone)
utc_to = datetime(2023, 8, 22, hour=22, tzinfo=timezone)
# get bars from XAUUSD M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates = mt.copy_rates_range("XAUUSD", mt.TIMEFRAME_D1, utc_from, utc_to)


def bar_parameters(rate):
    open_price = rate['open']
    close_price = rate['close']
    high_price = rate['high']
    low_price = rate['low']
    direction = ''

    if open_price < close_price:
        direction = 'UP'
    elif open_price > close_price:
        direction = 'DOWN'
    else:
        "NO DIRECTION"

    return f'BAR DIRECTION: {direction} \n' \
           f'Open Price: {open_price} \n' \
           f'Close Price: {close_price}\n' \
           f'Highest Price: {high_price}\n' \
           f'Lowest Price: {low_price}'


bars_history = []
count_bars = 0
for rate in rates:
    current_data = bar_parameters(rate)
    count_bars += 1
    print()
    print(f'Bar: {count_bars}')
    print(current_data)
