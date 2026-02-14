import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.header("📈 Scenario Simulator")
    
    inv = st.sidebar.slider("Monthly Investment", 5000, 100000, 20000)
    m_return = st.sidebar.slider("Market Return (%)", 1, 20, 12)
    inflation = st.sidebar.slider("Inflation (%)", 1, 10, 6)
    
    data = []
    current_wealth = 0
    real_rate = (1 + m_return/100) / (1 + inflation/100) - 1
    
    for y in range(1, 21):
        current_wealth = (current_wealth + inv*12) * (1 + real_rate)
        data.append({"Year": 2026 + y, "Wealth": current_wealth})
        
    df = pd.DataFrame(data)
    fig = px.line(df, x="Year", y="Wealth", title="Wealth Projection (Inflation Adjusted)")
    st.plotly_chart(fig, use_container_width=True)