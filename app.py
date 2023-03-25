import streamlit as st
from streamlit_option_menu import option_menu
import stockpredictor as sp
import mystocks as mys
import economicdata as ed

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
    ed.economicdata()
if selected == "Stock Searcher":
    st.title("Stock Searcher")
    user_input = st.text_input('Enter Stock Ticker', 'NFLX')
    mys.mystocks(user_input)
if selected == "My Stocks":
    st.title("My Stocks")
    mys.mystocks('SPOT')
    mys.mystocks('AMZN')
    mys.mystocks('GOOGL')
if selected == "Stock Predictor":
    sp.stockpredictor()