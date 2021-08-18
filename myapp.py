import yfinance as yf
import pandas as pd 
import streamlit as st 
import altair as alt

st.write("""
# Stock Charts

Type in your preferred ticker and start/end dates below!


""")

st.text_input("search a Ticker:", "AMD",key="tickerSymbol")
st.text_input("input a start date:","2010-8-18" ,key="start_date")
st.text_input("input an end date:", "2021-8-18",key="end_date")

start_date = st.session_state.start_date
end_date = st.session_state.end_date

tickerSymbol = st.session_state.tickerSymbol
tickerData = yf.Ticker(tickerSymbol)
tickerChart = tickerData.history(period="1d", start = start_date, end = end_date)



st.line_chart(tickerChart.Close)
st.line_chart(tickerChart.Volume)