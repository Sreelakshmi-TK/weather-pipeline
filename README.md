# 🌦 Weather Analytics Pipeline

An end-to-end cloud-based weather analytics platform that collects real-time weather data, processes it through AWS services, stores historical data in Snowflake, and visualizes insights using Streamlit.

---

## 📌 Project Overview

This project automates the collection, storage, processing, and visualization of weather data for Kochi using a fully serverless architecture.

The pipeline fetches weather information at scheduled intervals, stores raw and processed data in AWS, loads historical records into Snowflake, and provides interactive analytics through a Streamlit dashboard.

---

## 🏗 Architecture

```text
EventBridge
    ↓
Weather Ingestion Lambda
    ↓
DynamoDB
    ↓
DynamoDB Streams
    ↓
Weather Stream Processor Lambda
    ↓
Amazon S3
    ↓
Snowflake Stage
    ↓
Snowpipe
    ↓
WEATHER_DATA Table
    ↓
Streamlit Dashboard
```

---

## 🚀 Features

* Automated weather data ingestion
* Event-driven serverless architecture
* DynamoDB stream processing
* Historical weather data storage in S3
* Automated Snowflake ingestion using Snowpipe
* Real-time analytics dashboard
* Temperature and humidity trend visualization
* Weather condition distribution analysis
* Auto-refreshing dashboard

---

## 🛠 Technology Stack

### AWS

* Amazon EventBridge
* AWS Lambda
* Amazon DynamoDB
* DynamoDB Streams
* Amazon S3
* IAM

### Data Warehouse

* Snowflake
* Snowpipe
* External Stage
* Storage Integration

### Visualization

* Streamlit
* Plotly
* Pandas

### Language

* Python

---

## 📂 Project Structure

```text
weather-pipeline/
│
├── ingestion_lambda/
│   ├── lambda_function.py
│   └── requirements.txt
│
├── stream_processor/
│   ├── lambda_function.py
│   └── requirements.txt
│
├── dashboard/
│   ├── app.py
│   ├── snowflake_connection.py
│   ├── requirements.txt
│   └── .streamlit/
│
├── .gitignore
└── README.md
```

---

## ⚙ Workflow

### 1. Data Ingestion

EventBridge triggers the Weather Ingestion Lambda every 15 minutes.

The Lambda:

* Calls the weather API
* Retrieves current weather data
* Stores the weather record in DynamoDB

---

### 2. Stream Processing

DynamoDB Streams capture newly inserted weather records.

The Stream Processor Lambda:

* Reads stream events
* Converts records to JSON
* Stores files in Amazon S3

---

### 3. Snowflake Ingestion

Snowflake:

* Connects to S3 using Storage Integration
* Reads weather JSON files through an External Stage
* Loads records automatically using Snowpipe

---

### 4. Analytics Dashboard

Streamlit connects to Snowflake and displays:

* Latest temperature
* Latest humidity
* Current weather condition
* Historical weather records
* Temperature trends
* Humidity trends
* Weather distribution analytics

---

## 📊 Dashboard Visualizations

### KPI Cards

* Current Temperature
* Current Humidity
* Current Weather
* Total Records

### Trend Analysis

* Temperature Over Time
* Humidity Over Time

### Distribution Analysis

* Weather Condition Distribution

### Data Table

* Latest Weather Records

---

## 🔒 Security

Sensitive credentials are not stored in source code.

The dashboard uses:

* Streamlit Secrets
* Git Ignore Rules
* IAM Roles and Policies
* Snowflake Storage Integration

---

## ▶ Running the Dashboard

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 📈 Future Enhancements

* Multi-city weather monitoring
* Forecast analytics
* Weather anomaly detection
* Automated alert notifications
* Machine learning-based weather prediction
* Docker deployment
* CI/CD pipeline implementation

---

## 👩‍💻 Author

Sreelakshmi T K

B.Tech Artificial Intelligence and Data Science

Passionate about Data Engineering, Cloud Computing, Machine Learning, and Analytics.
