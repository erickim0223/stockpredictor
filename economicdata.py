from datetime import date
import pandas_datareader as pdr
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def economicdata():
    today = date.today()
    today_str = date.strftime(today, "%m-%d-%Y")
    st.title("Economic Data " + today_str)

    st.subheader("Unemployment Rate")

    start_date = date(2018, 1, 1)
    
    data_source = 'fred'
    unemployment_rate_code = 'UNRATE'

    unemployment_rate_df = pdr.DataReader(unemployment_rate_code, data_source, start_date)

    size = unemployment_rate_df.shape[0]

    curr_unemp_rate = str(unemployment_rate_df['UNRATE'][size - 1])
    last_date = date.strftime(unemployment_rate_df.index[size - 1], "%m-%d-%Y")

    st.write("As of " + last_date + " - Unemployment Rate: " + curr_unemp_rate)

    fig= px.line(unemployment_rate_df, x=unemployment_rate_df.index, y='UNRATE', render_mode='webg1')

    fig.update_layout(
        yaxis_title='Unemployment Rate %',
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