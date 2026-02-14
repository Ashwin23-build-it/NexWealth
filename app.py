import streamlit as st

# MUST BE THE FIRST COMMAND
st.set_page_config(page_title="NexWealth", page_icon="💰", layout="wide")

# Custom CSS for that Next.js / Tailwind Look
st.markdown("""
    <style>
    .stMetric { background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; }
    div[data-testid="stSidebarNav"] { background-color: #020617; }
    .main-header { font-size: 3rem; font-weight: 800; color: #10b981; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.sidebar.title("🏢 NexWealth")
    st.sidebar.caption("Build Wealth With Intelligence")
    
    # Simple Landing Page Logic
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar Navigation
    menu = ["Home", "Dashboard", "Goal Planner", "Scenario Simulator", "AI Assistant"]
    choice = st.sidebar.radio("Go to", menu)

    if choice == "Home":
        st.markdown("<h1 class='main-header'>Build Wealth With Intelligence.</h1>", unsafe_allow_html=True)
        st.write("### Your professional AI-powered wealth strategist.")
        if st.button("Get Started →"):
            st.info("Select 'Dashboard' from the sidebar to begin.")
            
    elif choice == "Dashboard":
        import pages.dashboard as dash
        dash.show()
    elif choice == "Goal Planner":
        import pages.goals as goals
        goals.show()
    elif choice == "Scenario Simulator":
        import pages.simulator as sim
        sim.show()
    elif choice == "AI Assistant":
        import pages.assistant as ai
        ai.show()

if __name__ == "__main__":
    main()
   
