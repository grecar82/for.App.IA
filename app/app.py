import streamlit as st
from utils.data_loader import load_data
from components.charts import plot_chart

# App title
st.set_page_config(page_title="My Streamlit App", layout="wide")
st.title("📊 My for.app.IA Streamlit Dashboard")

# Load data
try:
    df = load_data("data/sample_data.csv")
    st.success("Data loaded successfully!")
except FileNotFoundError:
    st.error("Data file not found.")
    st.stop()

# Display chart
plot_chart(df)