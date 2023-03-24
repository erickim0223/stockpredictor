import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as dt
import yfinance as yfin
from keras.models import load_model
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import date
import plotly.graph_objs as go 

def stocksearcher():
    st.title("Stock Searcher")
    today = date.today()

    user_input = st.text_input('Enter Stock Ticker', 'NFLX')
    df = web.get_data_yahoo(user_input, start='2010-01-01', end=today)
    df = df.drop(['Adj Close'], axis = 1)


    #Describing Data
    st.subheader(user_input + ' Stock Chart')

    fig=go.Figure()

    fig.add_trace(go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'], name = 'market data'))

    fig.update_layout(
        yaxis_title='Stock Price (USD per Shares)'
    )
    
    st.write(fig)