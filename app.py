import streamlit as st
import holidays
from streamlit_option_menu import option_menu
import stockpredictor as sp
import mystocks as mys
import economicdata as ed
from datetime import date

#Nav bar
with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Economic Data", "Stock Searcher", "My Stocks", "Stock Predictor"],
        icons = ["clipboard-data", "search", "list", "graph-up-arrow"],
        menu_icon = "cast",
        default_index = 0,
    )

if selected == "Economic Data":
    today = date.today()
    today_str = date.strftime(today, "%m-%d-%Y")
    st.title("Economic Data " + today_str)
    ed.economicdata("Unemployment Rate", "UNRATE")
    ed.economicdata("Inflation Rate", "CORESTICKM159SFRBATL")
    ed.economicdata("Federal Funds Effective Rate", "FEDFUNDS")
    ed.economicdata("10 Year Treasury Rate", "DGS10")
    ed.economicdata("2's 10's Spread", "T10Y2Y")
    ed.snp_gdp("S&P 500", "SP500")
    ed.snp_gdp("Real Gross Domestic Product", "GDPC1")
if selected == "Stock Searcher":
    st.title("Stock Searcher")
    user_input = st.text_input('Enter Stock Ticker', 'NFLX')
    mys.mystocks(user_input)
if selected == "My Stocks":
    st.title("My Stocks")
    mys.mystocks('SPOT')
    mys.mystocks('AMZN')
    mys.mystocks('GOOGL')
    mys.mystocks('BAC')
if selected == "Stock Predictor":
    sp.stockpredictor()