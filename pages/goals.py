import streamlit as st
import pandas as pd

def show():
    st.header("🎯 Goal Planner")
    
    with st.form("goal_form"):
        name = st.text_input("Goal Name", "Buying a Home")
        target = st.number_input("Target Amount (₹)", value=5000000)
        years = st.slider("Time Horizon (Years)", 1, 30, 10)
        returns = st.slider("Expected Return (%)", 5, 20, 12)
        submit = st.form_submit_button("Calculate SIP")

    if submit:
        n = years * 12
        r = (returns / 100) / 12
        # SIP Formula: P = FV / [((1+r)^n - 1) / r * (1+r)]
        sip = target / ((((1 + r)**n - 1) / r) * (1 + r))
        
        st.success(f"To reach ₹{target:,} in {years} years, you need a monthly SIP of:")
        st.title(f"₹{int(sip):,}")