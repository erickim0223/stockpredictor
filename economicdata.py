from datetime import date
import pandas_datareader as pdr
import streamlit as st
import matplotlib.pyplot as plt

def economicdata():
    st.title("Economic Data")

    today = date.today()
    today_str = date.strftime(today, "%m-%d-%Y")
    st.subheader("Today's Date: " + today_str)

    start_date = date(2018, 1, 1)
    
    data_source = 'fred'
    unemployment_rate_code = 'UNRATE'

    unemployment_rate_df = pdr.DataReader(unemployment_rate_code, data_source, start_date)

    size = unemployment_rate_df.shape[0]

    unemployment_rates = []
    for i in range(size):
        unemployment_rates.append(unemployment_rate_df['UNRATE'][i])

    curr_unemp_rate = str(unemployment_rate_df['UNRATE'][size - 1])
    last_date = date.strftime(unemployment_rate_df.index[size - 1], "%m-%d-%Y")

    st.write("As of " + last_date + ", Unemployment Rate: " + curr_unemp_rate)
    fig = plt.figure(figsize = (12, 6))
    plt.plot(unemployment_rates, 'b', label = 'Unemployment Rate')
    plt.ylabel('Unemployment Rate %')
    plt.legend()
    st.pyplot(fig)