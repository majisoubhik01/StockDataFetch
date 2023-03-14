import pandas as pd
import pandas_datareader as dr
from datetime import date
import numpy as np
from yahoofinancials import YahooFinancials
import streamlit as st

sel = st.selectbox('Pick One',['IT','AUTO'])

if st.button("Get Data"):
  if sel == "IT":
    tickers = np.array(['TCS.NS','TECHM.NS','WIPRO.NS',
                    'HCLTECH.NS','MPHASIS.NS','INFY.NS',
                    'LT.NS', 'SUBEXLTD.NS', 'NUCLEUS.NS'])
  elif sel == "AUTO":
    tickers = np.array(['M&M.NS','MARUTI.NS','TATAMOTORS.NS','EICHERMOT.NS',
                    'BAJAJ-AUTO.NS','HEROMOTOCO.NS','TIINDIA.NS',
                    'TVSMOTOR.NS', 'ASHOKLEY.NS', 'BHARATFORG.NS'])
  
  yahoo_financials = YahooFinancials(tickers)

  #start_date = st.date_input('Enter Start Date')
  #st.write(type(start_date))
  data = yahoo_financials.get_historical_price_data(start_date='2018-01-01', 
                                                  end_date='2022-12-31', 
                                                  time_interval='daily')

  prices_df = pd.DataFrame({a: {x['formatted_date']: x['close'] for x in data[a]['prices']} for a in tickers})

  st.table(prices_df.head())
