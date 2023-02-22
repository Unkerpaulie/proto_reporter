import streamlit as st
import pandas as pd

st.title("The Streamlit App")
st.write("Welcome to my app")

debt_data = pd.read_csv("debt_data.csv")
activity_data = pd.read_csv("activity_data.csv")
transaction_data = pd.read_csv("transaction_data.csv")

st.write(debt_data)

# setup sidebar
# print(collectors)
st.sidebar.header("Filters")
collectors = st.sidebar.multiselect("Collectors", options=sorted(debt_data["collector"].unique()), default=sorted(debt_data["collector"].unique()))
sectors = st.sidebar.multiselect("Sectors", options=sorted(debt_data["sector"].unique()), default=sorted(debt_data["sector"].unique()))
