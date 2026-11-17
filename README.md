# Data Cleaning & Reporting Automation

A Python + Streamlit internship project that cleans CSV data and generates automated reports.

## Features
- Upload a CSV or use the included sample dataset.
- Inspect missing values and duplicate rows.
- Trim whitespace; standardize email and city formatting.
- Optionally treat negative numeric values as missing.
- Treat ages above 100 as invalid when an Age column exists.
- Fill missing numeric values with the median.
- Standardize date columns.
- Compare original and cleaned data.
- Download cleaned CSV, summary CSV, and Excel report.

## Run the project
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Run `pip install -r requirements.txt`.
4. Run `streamlit run app.py`.
5. Open the local URL shown in the terminal (usually http://localhost:8501).

## Folder structure
- `app.py`: Streamlit application
- `requirements.txt`: dependencies
- `data/messy_customer_data.csv`: synthetic sample data
- `PROJECT_REPORT.md`: internship report

The included customer records are synthetic demonstration data, not real customer information. Review cleaning rules before using them on real data.
