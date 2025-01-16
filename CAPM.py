import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title= 'CAMP',
                   page_icon='chart_with_upwards_trend')
st.title('CAPITAL ASSET PRICING MODEL')
#GETTING INPUT
st.multiselect("choose stocks", 'AAPL', 'BA', 'MGM', 'AMZN', 'IBM', 'TSLA', 'GOOG', 'sp500')
import streamlit as st

# Define the list of options
options = ['AAPL', 'BA', 'MGM', 'AMZN', 'IBM', 'TSLA', 'GOOG', 'sp500']

# Use st.multiselect with the correct syntax
selected_stocks = st.multiselect("Choose stocks", options, default=['AAPL', 'BA', 'MGM', 'AMZN', 'IBM', 'TSLA', 'GOOG', 'sp500'])

