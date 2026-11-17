import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Data Cleaning & Reporting Automation", page_icon="🧹", layout="wide")
st.title("🧹 Data Cleaning & Reporting Automation")
st.caption("Clean CSV data, inspect quality issues, and generate reports.")

uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
try:
    original = pd.read_csv(uploaded) if uploaded else pd.read_csv("data/messy_customer_data.csv")
except Exception as e:
    st.error(f"Could not read file: {e}")
    st.stop()
if original.empty:
    st.error("The dataset is empty.")
    st.stop()

st.sidebar.header("Cleaning options")
do_trim = st.sidebar.checkbox("Trim spaces; standardize email/city", True)
do_fill = st.sidebar.checkbox("Fill missing numeric values with median", True)
do_dupes = st.sidebar.checkbox("Remove exact duplicate rows", True)
do_negative = st.sidebar.checkbox("Treat negative numeric values as missing", True)

clean = original.copy()
rows_before = len(clean)
missing_before = int(clean.isna().sum().sum())
dupes_before = int(clean.duplicated().sum())
clean = clean.replace(r"^\\s*$", np.nan, regex=True)

if do_trim:
    for col in clean.select_dtypes(include="object").columns:
        clean[col] = clean[col].astype("string").str.strip()
        if "email" in col.lower():
            clean[col] = clean[col].str.lower()
        elif "city" in col.lower():
            clean[col] = clean[col].str.title()

if do_negative:
    for col in clean.select_dtypes(include="number").columns:
        clean.loc[clean[col] < 0, col] = np.nan

for col in clean.columns:
    if col.lower() == "age":
        clean.loc[pd.to_numeric(clean[col], errors="coerce") > 100, col] = np.nan
    if "date" in col.lower():
        clean[col] = pd.to_datetime(clean[col], errors="coerce", format="mixed").dt.strftime("%Y-%m-%d")

if do_fill:
    for col in clean.select_dtypes(include="number").columns:
        if clean[col].isna().any() and clean[col].notna().any():
            clean[col] = clean[col].fillna(clean[col].median())
if do_dupes:
    clean = clean.drop_duplicates().reset_index(drop=True)

missing_after = int(clean.isna().sum().sum())
dupes_after = int(clean.duplicated().sum())
summary = pd.DataFrame({"Metric":["Rows before","Rows after","Rows removed","Missing cells before","Missing cells after","Duplicate rows before","Duplicate rows after"],
                        "Value":[rows_before,len(clean),rows_before-len(clean),missing_before,missing_after,dupes_before,dupes_after]})

st.subheader("1. Data quality overview")
a,b,c,d = st.columns(4)
a.metric("Original rows", rows_before)
b.metric("Cleaned rows", len(clean))
c.metric("Missing cells", f"{missing_before} → {missing_after}")
d.metric("Duplicate rows", f"{dupes_before} → {dupes_after}")

l,r = st.columns(2)
with l:
    st.markdown("**Original data**")
    st.dataframe(original.head(10), use_container_width=True)
with r:
    st.markdown("**Cleaned data**")
    st.dataframe(clean.head(10), use_container_width=True)

st.subheader("2. Missing values by column")
fig, ax = plt.subplots(figsize=(9,3))
original.isna().sum().plot(kind="bar", ax=ax)
ax.set_ylabel("Missing cells")
ax.grid(axis="y", alpha=.2)
plt.xticks(rotation=35, ha="right")
st.pyplot(fig)
plt.close(fig)

st.subheader("3. Numeric summary")
numeric = clean.select_dtypes(include="number")
if not numeric.empty:
    st.dataframe(numeric.describe().round(2), use_container_width=True)
    col = st.selectbox("Select numeric column", list(numeric.columns))
    fig, ax = plt.subplots(figsize=(8,3))
    numeric[col].dropna().plot(kind="hist", bins=10, ax=ax)
    ax.set_title(f"Distribution of {col}")
    st.pyplot(fig)
    plt.close(fig)
else:
    st.info("No numeric columns found.")

st.subheader("4. Automated cleaning report")
st.dataframe(summary, hide_index=True, use_container_width=True)
st.download_button("Download cleaned CSV", clean.to_csv(index=False).encode(), "cleaned_data.csv", "text/csv")
st.download_button("Download summary CSV", summary.to_csv(index=False).encode(), "cleaning_summary.csv", "text/csv")

buffer = BytesIO()
with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    clean.to_excel(writer, index=False, sheet_name="Cleaned Data")
    summary.to_excel(writer, index=False, sheet_name="Cleaning Summary")
st.download_button("Download Excel report", buffer.getvalue(), "cleaning_report.xlsx",
                   "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
st.info("The included customer dataset is synthetic sample data. Review cleaning rules before applying them to real data.")
