import pandas as pd
import pandas_datareader as dr
from datetime import date
import numpy as np
from yahoofinancials import YahooFinancials
import streamlit as st
tickers = np.array(['TCS.NS','TECHM.NS','MINDTREE.NS','WIPRO.NS',
                    'HCLTECH.NS','MPHASIS.NS','INFY.NS',
                    'LT.NS', 'SUBEXLTD.NS', 'NUCLEUS.NS'])

yahoo_financials = YahooFinancials(tickers)

start_date = st.date_input('Enter Start Date')
st.write(type(start_date))
data = yahoo_financials.get_historical_price_data(start_date=str(start_date), 
                                                  end_date=str(date.today()), 
                                                  time_interval='daily')

prices_df = pd.DataFrame({
    a: {x['formatted_date']: x['close'] for x in data[a]['prices']} for a in tickers})

st.table(prices_df.head())