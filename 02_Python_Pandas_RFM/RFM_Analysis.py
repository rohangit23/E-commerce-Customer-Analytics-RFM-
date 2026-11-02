
import pandas as pd
import numpy as np

# ==========================================
# STEP 1: LOAD THE CLEANED DATASET
# ==========================================

df = pd.read_csv("RetailCleaned.csv", header=None)

df.columns = [
    "Invoice", "StockCode", "Description", "Quantity",
    "InvoiceDate", "Price", "Customer_ID", "Country",
    "SourceSheet"
]

# ==========================================
# STEP 2: DATA TYPE CONVERSION
# ==========================================

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("Dataset Shape:", df.shape)
df.info()

# ==========================================
# STEP 3: FILTER DATA FOR RFM ANALYSIS
# ==========================================

rfm_data = df[
    (df["Customer_ID"].notna()) &
    (df["Quantity"] > 0)
].copy()

# Reference date
snapshot_date = pd.to_datetime("2011-12-10")

# ==========================================
# STEP 4: CALCULATE RFM METRICS
# ==========================================

rfm = rfm_data.groupby("Customer_ID").agg(
    Recency=("InvoiceDate",
             lambda x: (snapshot_date - x.max()).days),

    Frequency=("Invoice", "nunique"),

    Monetary=("Price",
              lambda x: (
                  x * rfm_data.loc[x.index, "Quantity"]
              ).sum())
).reset_index()

print(rfm.head())

# ==========================================
# STEP 5: ASSIGN RFM SCORES
# ==========================================

rfm["R_Score"] = pd.qcut(
    rfm["Recency"], 5, labels=[5, 4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5, labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5, labels=[1, 2, 3, 4, 5]
).astype(int)

# ==========================================
# STEP 6: CUSTOMER SEGMENTATION
# ==========================================

def segment_customer(row):

    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "Champions"

    elif row["R_Score"] >= 3 and row["F_Score"] >= 3:
        return "Loyal"

    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"

    elif row["R_Score"] >= 4 and row["F_Score"] <= 2:
        return "New"

    elif row["R_Score"] == 3 and row["F_Score"] <= 2:
        return "Needs Attention"

    else:
        return "Lost"


rfm["Segment"] = rfm.apply(segment_customer, axis=1)

# ==========================================
# STEP 7: CHURN INDICATOR
# ==========================================

rfm["IsChurned"] = rfm["Recency"] > 90

# ==========================================
# STEP 8: PREPARE TRANSACTION DATA
# ==========================================

df = df[
    (df["Customer_ID"].notna()) &
    (df["Quantity"] > 0)
].copy()

df["InvoiceMonth"] = (
    df["InvoiceDate"].dt.to_period("M").dt.to_timestamp()
)

df["Revenue"] = df["Quantity"] * df["Price"]

# ==========================================
# STEP 9: MERGE RFM RESULTS
# ==========================================

df_final = df.merge(
    rfm[
        [
            "Customer_ID", "Recency", "Frequency", "Monetary",
            "R_Score", "F_Score", "M_Score",
            "Segment", "IsChurned"
        ]
    ],
    on="Customer_ID",
    how="left"
)

# ==========================================
# STEP 10: EXPORT FINAL DATASET
# ==========================================

df_final.to_excel(
    "EcommerceDashboardData.xlsx",
    index=False
)

print("RFM Analysis Completed Successfully!")
