import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh
from snowflake_connection import get_connection

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Weather Analytics Dashboard",
    page_icon="🌦",
    layout="wide"
)

# Auto Refresh every minute
st_autorefresh(
    interval=60000,
    key="weather_refresh"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌦 Weather Analytics Dashboard")
st.markdown("Real-time weather monitoring powered by AWS, Snowflake and Streamlit")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data(ttl=60)
def load_data():
    conn = get_connection()

    query = """
    SELECT
        CITY,
        TIMESTAMP,
        TEMPERATURE,
        HUMIDITY,
        WEATHER
    FROM WEATHER_DATA
    ORDER BY TIMESTAMP DESC
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df

df = load_data()

# -----------------------------
# Data Preparation
# -----------------------------
df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"])

latest = df.iloc[0]

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌡 Temperature",
        f"{latest['TEMPERATURE']:.1f} °C"
    )

with col2:
    st.metric(
        "💧 Humidity",
        f"{latest['HUMIDITY']} %"
    )

with col3:
    st.metric(
        "☁ Weather",
        latest["WEATHER"]
    )

with col4:
    st.metric(
        "📊 Total Records",
        len(df)
    )

st.divider()

# -----------------------------
# Temperature Trend
# -----------------------------
st.subheader("🌡 Temperature Trend")

temp_fig = px.line(
    df.sort_values("TIMESTAMP"),
    x="TIMESTAMP",
    y="TEMPERATURE",
    title="Temperature Over Time"
)

st.plotly_chart(
    temp_fig,
    use_container_width=True
)

# -----------------------------
# Humidity Trend
# -----------------------------
st.subheader("💧 Humidity Trend")

humidity_fig = px.line(
    df.sort_values("TIMESTAMP"),
    x="TIMESTAMP",
    y="HUMIDITY",
    title="Humidity Over Time"
)

st.plotly_chart(
    humidity_fig,
    use_container_width=True
)

# -----------------------------
# Weather Distribution
# -----------------------------
left_col, right_col = st.columns([1, 2])

with left_col:

    st.subheader("☁ Weather Distribution")

    weather_count = (
        df["WEATHER"]
        .value_counts()
        .reset_index()
    )

    weather_count.columns = [
        "Weather",
        "Count"
    ]

    weather_fig = px.pie(
        weather_count,
        names="Weather",
        values="Count",
        title="Weather Conditions"
    )

    st.plotly_chart(
        weather_fig,
        use_container_width=True
    )

with right_col:

    st.subheader("📋 Latest Weather Records")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )

# -----------------------------
# Summary Statistics
# -----------------------------
st.subheader("📈 Weather Summary")

summary_df = (
    df.groupby("CITY")
      .agg(
          Average_Temperature=("TEMPERATURE", "mean"),
          Average_Humidity=("HUMIDITY", "mean"),
          Records=("CITY", "count")
      )
      .reset_index()
)

st.dataframe(
    summary_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "Architecture: EventBridge → Lambda → DynamoDB → DynamoDB Streams → Lambda → S3 → Snowflake → Streamlit"
)