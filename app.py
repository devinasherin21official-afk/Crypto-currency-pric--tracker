import pandas as pd
import streamlit as st

st.set_page_config(page_title="Crypto Tracker", layout="wide")

st.title("🚀 Cryptocurrency Price Tracker")

df = pd.read_csv("crypto_prices.csv")

search = st.text_input("Search Cryptocurrency")

if search:
    df = df[df["Name"].str.contains(search, case=False)]

st.metric("Total Coins Tracked", len(df))

st.dataframe(df, use_container_width=True)
st.subheader("Most Expensive Coin")
st.write(df.loc[df["Price"].idxmax()])
if st.button("Refresh Data"):
    st.rerun()