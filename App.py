
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="WHAT IF?",
    page_icon="💡",
    layout="wide"
)

# Main Title
st.title("💡 WHAT IF?")
st.subheader("Engineering Decision Support Platform")

st.write(
    "Simulate different scenarios, "
    "compare alternatives, and make better decisions."
)

st.divider()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page",
    ["Dashboard", "New Analysis", "Scenario Comparison"]
)

if page == "Dashboard":

    st.header("Welcome to WHAT IF?")

    st.write(
        "Explore possible decisions before "
        "implementing them in real life."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Scenarios", "0")
    col2.metric("Feasible Solutions", "0")
    col3.metric("Analyses", "0")

    st.divider()

    st.subheader("Our First Application")

    st.write(
        "Classroom Allocation: "
        "Testing different classroom assignments "
        "to improve resource utilization."
    )

elif page == "New Analysis":

    st.header("Create a New Analysis")

    st.info(
        "This section will allow users to enter "
        "data and create different scenarios."
    )

elif page == "Scenario Comparison":

    st.header("Compare Scenarios")

    st.info(
        "This section will compare simulation "
        "results and recommend the best alternative."
    )
