# 🛒 E-commerce Customer Analytics – RFM Analysis

### 📊 From Raw Transaction Data to Actionable Business Insights

An end-to-end **E-commerce Customer Analytics** project built using **SQL, Python (Pandas), and Microsoft Power BI** to understand customer purchasing behaviour, analyze revenue performance, identify valuable customer segments, and generate actionable business insights.

---

## 🌟 Project Overview

Understanding customers is essential for improving business performance and customer retention.

This project analyzes historical online retail transactions to uncover meaningful insights about customer purchasing patterns, spending behaviour, customer value, and churn.

The project follows a complete data analytics workflow, starting with SQL-based data cleaning, followed by Python-based RFM analysis, and ending with an interactive Power BI dashboard.

### 🔄 Project Workflow

**SQL Data Cleaning → Python Pandas & RFM Analysis → Power BI Dashboard**

---

## 🧰 Tech Stack & Tools

| Category | Technologies |
|---|---|
| Database | Microsoft SQL Server |
| Query Language | SQL |
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Development Environment | Jupyter Notebook |
| Business Intelligence | Microsoft Power BI |
| Data Transformation | Power Query |
| Data Visualization | Power BI Visuals |
| Calculations | DAX |

---

## 📁 Project Structure

```text
E-commerce-Customer-Analytics-RFM/
│
├── 01_SQL_Data_Cleaning/
│   ├── SQL_Queries/
│   │   └── SQL_Data_Cleaning.sql
│   └── README.md
│
├── 02_Python_Pandas_RFM/
│   ├── RFM_Analysis.py
│   └── README.md
│
├── 03_PowerBI_Dashboard/
│   ├── Screenshots/
│   └── README.md
│
├── LICENSE
└── README.md
```

---

# 🔹 1. SQL – Data Cleaning & Preparation

**Objective:** Transform raw retail transaction data into a structured and analysis-ready dataset.

### ⚙️ Activities Performed

- Imported two Online Retail II datasets into Microsoft SQL Server.
- Combined datasets using `UNION ALL`.
- Explored table structures and transaction records.
- Identified missing descriptions and customer IDs.
- Checked invalid quantities and non-positive prices.
- Performed duplicate identification using `GROUP BY` and `HAVING`.
- Applied Common Table Expressions (CTEs).
- Used `ROW_NUMBER()` for duplicate handling.
- Created and validated the final cleaned table.

### 💡 SQL Concepts Applied

`SELECT` · `WHERE` · `UNION ALL` · `GROUP BY` · `HAVING` · `CASE` · `TRY_CONVERT()` · `COALESCE()` · `CTE` · `ROW_NUMBER()`

📂 **Folder:** `01_SQL_Data_Cleaning/`

---

# 🔹 2. Python – Pandas & RFM Customer Segmentation

**Objective:** Analyze customer purchasing behaviour and classify customers based on their transaction history.

### 📊 RFM Analysis

RFM stands for:

| Metric | Description |
|---|---|
| 🕒 Recency | How recently a customer made a purchase |
| 🔁 Frequency | How frequently a customer made purchases |
| 💰 Monetary | How much money a customer spent |

### ⚙️ Activities Performed

- Loaded the cleaned retail dataset using Pandas.
- Converted invoice dates into datetime format.
- Filtered transactions with valid Customer IDs and positive quantities.
- Calculated Recency, Frequency, and Monetary metrics.
- Assigned customer scores from 1 to 5.
- Applied `pd.qcut()` for RFM scoring.
- Developed customer segmentation logic.
- Created a customer churn indicator using a 90-day Recency threshold.
- Calculated monthly revenue.
- Merged RFM metrics with transaction-level data.
- Exported the final dataset for Power BI reporting.

### 🎯 Customer Segments Identified

| Segment | Description |
|---|---|
| 🏆 Champions | Recent, frequent, and high-value customers |
| 💎 Loyal | Customers with consistent purchasing behaviour |
| ⚠️ At Risk | Previously active customers with declining activity |
| 🆕 New | Recently acquired customers |
| 🔔 Needs Attention | Customers who may need engagement |
| ❌ Lost | Customers with low recent engagement |

📂 **Folder:** `02_Python_Pandas_RFM/`

---

# 🔹 3. Power BI – Interactive Business Intelligence Dashboard

**Objective:** Convert customer and transaction data into interactive visual reports for business analysis and decision-making.

### 📈 Dashboard 1 – Business Overview

Key performance indicators:

- 👥 Total Customers
- 💰 Total Revenue
- 📉 Customer Churn Percentage
- 💵 Average Customer Value

Additional visualizations:

- Revenue by Customer Segment
- Monthly Revenue Trends
- Quarterly Revenue Trends
- Yearly Revenue Trends
- Customer Performance Analysis

### 📊 Dashboard 2 – RFM Analysis

- Segment Performance Summary
- Country Performance Summary
- Average Customer Value by Segment
- Top 5 Countries by Average Customer Value
- Customer Churn Trends
- RFM Score Analysis

### 🎛️ Interactive Features

- Month, Quarter, and Year slicers
- Country and Customer Segment filters
- Bookmarks and Buttons for visual navigation
- Conditional Formatting
- Interactive charts and matrix visualizations

### 🖼️ Dashboard Screenshots

Explore the dashboard screenshots in:

[`03_PowerBI_Dashboard/Screenshots/`](03_PowerBI_Dashboard/Screenshots/)

📂 **Folder:** `03_PowerBI_Dashboard/`

---

## 🎯 Key Business Objectives

This project aims to:

1. Understand customer purchasing patterns.
2. Identify high-value and loyal customers.
3. Recognize customers at risk of churn.
4. Analyze revenue across customer segments.
5. Evaluate country-wise customer performance.
6. Support customer retention and engagement strategies.
7. Enable data-driven business decisions.

---

## 📌 Project Highlights

- ✅ End-to-end data analytics workflow.
- ✅ SQL-based data cleaning and validation.
- ✅ Customer-level RFM analysis using Python.
- ✅ Six customer segments based on purchasing behaviour.
- ✅ Churn identification using a 90-day threshold.
- ✅ Interactive Power BI dashboards.
- ✅ Business-focused reporting and visualizations.

---

## 📂 Data Availability

The project uses two Online Retail II transaction datasets (2009–2010 and 2010–2011).

Due to their large file sizes, the raw and cleaned CSV datasets are not included in this repository. SQL scripts and Python source code document the analysis workflow.

---

## 🚀 Future Enhancements

- Customer Lifetime Value (CLV) analysis.
- Customer retention strategy recommendations.
- Advanced customer purchasing behaviour analysis.
- Additional business performance KPIs.
- Automated reporting and dashboard updates.

---

## 👨‍💻 About the Author

**Rohan Prajapati**

🎓 B.Tech – Computer Science (Data Science Specialisation), 2026

Interested in Data Analytics, Business Intelligence, Customer Analytics, and Data-Driven Decision Making.

---

### ⭐ If you find this project interesting, feel free to explore the repository!

**Thank you for visiting!**
