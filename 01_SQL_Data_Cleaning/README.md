# E-commerce Customer Analytics – SQL Data Cleaning

## 1. Project Overview

This repository contains the SQL data cleaning stage of my E-commerce Customer Analytics project.

The main objective of this stage is to clean, consolidate, and prepare raw online retail transaction data using Microsoft SQL Server before performing customer analysis and visualization.

## 2. Tools & Technologies

- Microsoft SQL Server
- SQL Server Management Studio (SSMS)
- SQL

## 3. Dataset Description

The project uses two Online Retail II datasets:

- Online Retail Dataset (2009–2010)
- Online Retail Dataset (2010–2011)

Both datasets contain e-commerce transaction information, including invoice numbers, product details, quantities, transaction dates, prices, customer IDs, and countries.

**Note:** The original CSV files and final cleaned dataset are not included in this repository because of their large file sizes. The SQL scripts are provided to demonstrate the data preparation workflow.

## 4. SQL Data Cleaning Process

### Step 1: Database and Data Import
- Created the project database in SQL Server.
- Imported both raw retail datasets into separate tables.

### Step 2: Data Consolidation
- Combined both datasets into a single table using `UNION ALL`.
- Created the consolidated table `RetailCombined`.

### Step 3: Data Exploration
- Examined the dataset structure and column names.
- Checked total records and previewed transaction data.

### Step 4: Missing Value Analysis
- Identified missing product descriptions.
- Checked missing customer IDs.

### Step 5: Data Quality Checks
- Identified invalid or non-positive quantities.
- Checked non-positive product prices.
- Validated transaction dates and numeric data types.

### Step 6: Duplicate Detection
- Identified duplicate transaction records using `GROUP BY` and `HAVING`.
- Applied `ROW_NUMBER()` with a Common Table Expression (CTE) to handle duplicate records.

### Step 7: Final Dataset Creation
- Created the final cleaned table named `RetailCleaned`.
- Removed duplicate and invalid transaction records.
- Prepared the cleaned data for further analysis.

### Step 8: Data Validation
- Verified the final record count.
- Checked invalid quantities and prices.
- Validated duplicate records after cleaning.

## 5. SQL Concepts Applied

- SELECT, WHERE, ORDER BY
- UNION ALL
- GROUP BY and HAVING
- Aggregate Functions
- CASE Statements
- TRY_CONVERT()
- COALESCE()
- Common Table Expressions (CTEs)
- ROW_NUMBER() Window Function
- CREATE TABLE and SELECT INTO
- Data Cleaning and Validation

## 6. Project Files

| File | Description |
|---|---|
| SQL_Queries/SQL_Data_Cleaning.sql | Consolidated SQL queries used for data preparation |
| README.md | Project documentation |

## 7. Project Workflow

**SQL Data Cleaning → Python Pandas & RFM Analysis → Power BI Dashboard**

## 8. Next Stage

The next stage uses Python Pandas to perform customer-level analysis, calculate Recency, Frequency, and Monetary values, and segment customers based on their purchasing behaviour.

---

**Author:** Rohan Prajapati
