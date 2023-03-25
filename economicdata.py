from datetime import date
import pandas_datareader as pdr
import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yfin
import plotly.express as px

def economicdata(subheader, code):
    yfin.pdr_override()

    st.subheader(subheader)

    start_date = date(2018, 1, 1)
    
    data_source = 'fred'

    df = pdr.DataReader(code, data_source, start_date)

    size = df.shape[0]

    curr_val = str(df[code][size - 1])
    last_date = date.strftime(df.index[size - 1], "%m-%d-%Y")

    st.write("As of " + last_date + " - " + subheader + ": " + curr_val + "%")

    fig = px.line(df, x=df.index, y=code, render_mode='webg1')
    fig.update_layout(
        yaxis_title=subheader + ' (%)',
        xaxis_title='',
        hovermode='x unified'
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

def snp_gdp(subheader, code):
    yfin.pdr_override()

    st.subheader(subheader)

    start_date = date(2018, 1, 1)
    
    data_source = 'fred'

    df = pdr.DataReader(code, data_source, start_date)

    size = df.shape[0]

    curr_val = str(df[code][size - 1])
    last_date = date.strftime(df.index[size - 1], "%m-%d-%Y")

    st.write("As of " + last_date + " - " + subheader + ": " + curr_val)

    sec_to_last_date = date.strftime(df.index[size - 2], "%m-%d-%Y")
    price_diff = round(df[code][size - 1] - df[code][size - 2], 2)
    percent_diff = round((((df[code][size - 1] - df[code][size - 2])/df[code][size - 2]) * 100), 2)

    color = 'green'
    icon_str = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css" integrity="sha384-b6lVK+yci+bfDmaY1u0zE8YYJt0TZxLEAFyYSLHId4xoVvsrQu3INevFKo+Xir8e" crossorigin="anonymous">'
    if (price_diff > 0):
        price_diff = icon_str + "<p style='color: green;'>+" + str(price_diff) +  " (" + str(percent_diff) + "%) <i class='bi bi-arrow-up'></i> since " + sec_to_last_date + "</p>"
    else:
        color = 'red'
        price_diff = icon_str + "<p style='color: red;'>" + str(price_diff) +  " (" + str(percent_diff) + "%) <i class='bi bi-arrow-down'></i> since " + sec_to_last_date + "</p>"
    
    st.markdown(price_diff, unsafe_allow_html=True)

    fig = px.line(df, x=df.index, y=code, render_mode='webg1')
    fig.update_layout(
        yaxis_title=subheader,
        xaxis_title='',
        hovermode='x unified'
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
    
    fig['data'][0]['line']['color'] = color

    st.write(fig)