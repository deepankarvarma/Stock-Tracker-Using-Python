import streamlit as st
import yfinance as yf
import pandas as pd

# Set the page title
st.set_page_config(page_title='Stock Tracker', page_icon=':chart_with_upwards_trend:')
st.title("Stock Tracker")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://4kwallpapers.com/images/wallpapers/dark-background-abstract-background-network-3d-background-2560x1440-8324.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# Define a function to get the stock data
@st.cache_data
def get_stock_data(ticker):
    stock_data = yf.download(ticker)
    return stock_data

# Create a text input for the user to enter a stock ticker
ticker_input = st.sidebar.text_input('Enter a stock ticker (e.g. AAPL,INTC)', 'AAPL')
st.markdown(f"<h3>Visualization for {ticker_input}</h3>",unsafe_allow_html=True)
# Get the stock data for the entered ticker
stock_data = get_stock_data(ticker_input)

# Display the stock data in a line chart
st.line_chart(stock_data['Close'])

# Display the stock data in a table
st.write(stock_data)
