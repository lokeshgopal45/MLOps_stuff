import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime


st.title('Stock Market Analysis')
st.write(""" Welcome to My Stock Market Analysis App! """) 


start_date = st.date_input("Start Date", datetime.date(2000, 1, 1))
end_date = st.date_input("End Date", datetime.date(2100, 12, 31))

ticker_list = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
ticker = st.selectbox("Choose the Ticker Symbol", ticker_list)

ticker_data = yf.Ticker(ticker)
df = ticker_data.history(period='1d', start=start_date, end=end_date)

st.dataframe(df)


st.write(""" 
            ## Closing Price
""")

st.line_chart(df['Close'])