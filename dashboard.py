import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Farming AI Dashboard", layout="wide")

st.title("🌱 Sustainable Farming AI Dashboard")

# Fetch data
conn = sqlite3.connect("db/farming_memory.db")
df = pd.read_sql_query("SELECT * FROM agent_logs ORDER BY timestamp DESC", conn)
conn.close()

st.subheader("Recent Agent Recommendations")
st.dataframe(df)
