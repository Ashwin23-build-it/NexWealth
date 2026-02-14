import streamlit as st
import plotly.express as px

def show():
    st.header("Financial Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    income = col1.number_input("Monthly Income (₹)", value=100000)
    expenses = col2.number_input("Monthly Expenses (₹)", value=40000)
    emergency_fund = col3.number_input("Emergency Fund (₹)", value=200000)
    debt = col4.number_input("Monthly Debt EMI (₹)", value=10000)

    savings = income - expenses
    savings_rate = (savings / income) * 100
    
    # Health Score Logic
    score = 0
    score += 40 if savings_rate >= 30 else (savings_rate / 30) * 40
    score += 30 if emergency_fund >= (expenses * 6) else 15
    score += 30 if (debt / income) <= 0.3 else 10
    
    st.divider()
    m1, m2, m3 = st.columns(3)
    m1.metric("Savings Rate", f"{savings_rate:.1f}%")
    m2.metric("Financial Health", f"{int(score)}/100")
    m3.metric("Monthly Surplus", f"₹{savings:,}")

    # Chart
    fig = px.pie(values=[60, 20, 10, 10], names=["Equities", "Debt", "Gold", "Cash"], 
                 hole=0.5, title="Asset Allocation", color_discrete_sequence=px.colors.sequential.Greens_r)
    st.plotly_chart(fig)