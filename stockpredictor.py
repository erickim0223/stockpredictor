import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from datetime import date
import yfinance as yfin
from keras.models import load_model
import streamlit as st
from streamlit_option_menu import option_menu
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

def stockpredictor():
    yfin.pdr_override()

    st.title("Stock Trend Predictor")

    start_date = date(2018, 1, 1)
    today = date.today()


    user_input = st.text_input('Enter Stock Ticker', 'NFLX')
    df = web.get_data_yahoo(user_input, start=start_date, end=today)
    df = df.drop(['Adj Close'], axis = 1)

    #Visualizations
    st.subheader('Closing Price vs Time chart')
    fig = plt.figure(figsize = (12,6))
    plt.plot(df.Close)
    st.pyplot(fig)

    st.subheader('Closing Price vs Time chart with 100MA')
    ma100 = df.Close.rolling(100).mean()
    fig = plt.figure(figsize = (12,6))
    plt.plot(ma100)
    plt.plot(df.Close)
    st.pyplot(fig)

    st.subheader('Closing Price vs Time chart with 100MA & 200MA')
    ma100 = df.Close.rolling(100).mean()
    ma200 = df.Close.rolling(200).mean()
    fig = plt.figure(figsize = (12,6))
    plt.plot(ma100, 'r')
    plt.plot(ma200, 'g')
    plt.plot(df.Close, 'b')
    st.pyplot(fig)

    #Splitting Data into Training and Testing

    data_training = pd.DataFrame(df['Close'][0:int(len(df) * 0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df) * 0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)


    #Load my model
    model = load_model('keras_model.h5')

    #Testing Part

    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index = True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)

    scaler = scaler.scale_

    scale_factor = 1/scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    #Final Graph

    st.subheader('Predictions vs Original')
    fig2 = plt.figure(figsize = (12, 6))
    plt.plot(y_test, 'b', label = 'Original Price')
    plt.plot(y_predicted, 'r', label = 'Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig2)

    START = "2020-01-01"
    td = today.strftime("%Y-%m-%d")

    st.subheader("Stock Predictor")

    n_years = st.slider("Years of prediction:", 1, 4)
    period = n_years * 365

    @st.cache_data
    def load_data(ticker):
        data = yfin.download(ticker, START, td)
        data.reset_index(inplace=True)
        return data

    # data_load_state = st.text("Load data...")
    data = load_data(user_input)
    # data_load_state.text("Loading data...done!")

    # st.subheader("Raw data")
    # st.write(data.head())

    def plot_raw_data():
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig3.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig3.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig3)

    plot_raw_data()

    # Forecasting
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(
        columns = {
            "Date": "ds", 
            "Close": "y"
        }
    )

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader("Forecast Data")
    st.write(forecast.tail())

    st.write("Forecast Data")
    fig4 = plot_plotly(m, forecast)
    st.plotly_chart(fig4)

    st.write("Forecast Components")
    fig5 = m.plot_components(forecast)
    st.write(fig5)
