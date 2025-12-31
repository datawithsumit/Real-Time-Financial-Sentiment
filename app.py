import streamlit as st
import pandas as pd 
import time
import plotly.express as px
from sentiment_engine import get_live_data

st.set_page_config(page_title="MarketMood AI Dashboard", layout="wide")
st.title("🤖 MarketMood: Real-Time AI Sentiment Analysis")
st.markdown("This dashboard ingests live news feeds and uses **NLP** to track market sentiment.")

if "data" not in st.session_state:
    st.session_state["data"] = []

placeholder = st.empty()

for _ in range(200):
    new_record = get_live_data()
    st.session_state["data"].append(new_record)

    df = pd.DataFrame(st.session_state["data"])
    if len(df) > 20:
        df = df.tail(20)
    
    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)
        avg_sentiment = df["score"].mean()

        kpi1.metric(label="Latest Ticker", value=new_record["ticker"])
        kpi2.metric(label="Latest Mood", value=new_record["mood"], delta=f"{new_record['score']:.2f}")
        kpi3.metric(label="Avg Sentiment (Last 20)", value=f"{avg_sentiment:.2f}")

        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader("📉 Sentiment Trend")
            fig = px.line(df, x="time", y="score", color="ticker", markers=True)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.subheader("📰 Recent Headlines")
            st.dataframe(df[["time", "ticker", "headline", "mood"]].iloc[::-1]) # Show newest first

    # C. Wait for 1 second before next update
    time.sleep(1)
