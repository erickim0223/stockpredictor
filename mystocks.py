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
import plotly.express as px



def mystocks(stockname):
    today = date.today()
    df = web.get_data_yahoo(stockname, start='2010-01-01', end=today)

    #Describing Data
    st.subheader(stockname + ' Stock Chart')

    size = df.shape[0]
    last_date = date.strftime(df.index[size - 1], "%m-%d-%Y")
    curr_price = str(round(df['Close'][size - 1], 2))
    st.write("As of " + last_date + " - Stock Price: " + curr_price + " USD")

    sec_to_last_date = date.strftime(df.index[size - 2], "%m-%d-%Y")
    price_diff = round(df['Close'][size - 1] - df['Close'][size - 2], 2)
    percent_diff = round((((df['Close'][size - 1] - df['Close'][size - 2])/df['Close'][size - 2]) * 100), 2)

    icon_str = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css" integrity="sha384-b6lVK+yci+bfDmaY1u0zE8YYJt0TZxLEAFyYSLHId4xoVvsrQu3INevFKo+Xir8e" crossorigin="anonymous">'
    if (price_diff > 0):
        price_diff = icon_str + "<p style='color: green;'>+" + str(price_diff) +  " (" + str(percent_diff) + "%) <i class='bi bi-arrow-up'></i> since " + sec_to_last_date + "</p>"
    else:
        price_diff = icon_str + "<p style='color: red;'>-" + str(price_diff) +  " (" + str(percent_diff) + "%) <i class='bi bi-arrow-down'></i> since " + sec_to_last_date + "</p>"
    
    st.markdown(price_diff, unsafe_allow_html=True)

    fig= px.line(df, x=df.index, y='Close', render_mode='webg1')

    fig.update_layout(
        yaxis_title='Stock Price (USD per Shares)',
        xaxis_title=''
    )

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    st.write(fig)