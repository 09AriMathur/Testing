import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("📈 Sales Dashboard")

# Load sample data
@st.cache_data
def load_data():
    data = {
        "Date": pd.date_range("2025-06-01", periods=10).repeat(2),
        "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South"] * 2,
        "Salesperson": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie", "Alice"] * 2,
        "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop"] * 2,
        "Units Sold": np.random.randint(1, 15, 20),
        "Revenue": np.random.randint(1000, 10000, 20)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar filters
st.sidebar.header("🔎 Filters")
region = st.sidebar.multiselect("Select Region(s)", options=df["Region"].unique(), default=df["Region"].unique())
salesperson = st.sidebar.multiselect("Select Salesperson(s)", options=df["Salesperson"].unique(), default=df["Salesperson"].unique())

# Filtered Data
filtered_df = df[(df["Region"].isin(region)) & (df["Salesperson"].isin(salesperson))]

# KPIs
st.subheader("📌 Key Metrics")
st.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
st.metric("Units Sold", f"{filtered_df['Units Sold'].sum()}")

# Charts
st.subheader("📍 Revenue by Region")
rev_by_region = filtered_df.groupby("Region")["Revenue"].sum()
st.bar_chart(rev_by_region)

st.subheader("📅 Revenue Over Time")
rev_by_date = filtered_df.groupby("Date")["Revenue"].sum()
st.line_chart(rev_by_date)

# Data Table
st.subheader("🧾 Raw Data")
st.dataframe(filtered_df)

