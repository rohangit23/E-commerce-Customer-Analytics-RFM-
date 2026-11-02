# Python Pandas – RFM Customer Segmentation

## 1. Project Overview

This is the second stage of my E-commerce Customer Analytics project. Python Pandas is used to analyze customer purchasing behaviour and perform RFM (Recency, Frequency, Monetary) analysis.

## 2. Tools & Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook

## 3. Data Processing Workflow

1. Loaded the cleaned retail dataset using Pandas.
2. Assigned column names and checked dataset dimensions and data types.
3. Converted InvoiceDate into datetime format.
4. Filtered records with valid Customer IDs and positive quantities.
5. Calculated Recency, Frequency, and Monetary values for each customer.
6. Assigned RFM scores from 1 to 5.
7. Segmented customers into business categories.
8. Created an IsChurned indicator using a 90-day Recency threshold.
9. Merged RFM metrics back into transaction data.
10. Calculated monthly revenue and exported the final analysis dataset.

## 4. Customer Segments

- Champions
- Loyal
- At Risk
- New
- Needs Attention
- Lost

## 5. Key Python Concepts

- Pandas DataFrames
- Data Filtering
- GroupBy and Aggregation
- Lambda Functions
- Datetime Conversion
- `pd.qcut()`
- `nunique()`
- `merge()`
- Customer Segmentation

## 6. Output

The processed customer analytics dataset is prepared for the Power BI dashboard.

## 7. Project Workflow

**SQL Data Cleaning → Python Pandas & RFM Analysis → Power BI Dashboard**

## Author
Rohan Prajapati
