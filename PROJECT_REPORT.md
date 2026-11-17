# PROJECT REPORT
## Data Cleaning & Reporting Automation

### 1. Abstract
This project automates common data-cleaning tasks and produces summary reports. A Streamlit dashboard accepts a CSV file, displays data-quality information, applies configurable cleaning rules, and exports cleaned data and reports.

### 2. Problem statement
Raw datasets may contain missing values, duplicate records, inconsistent text formatting, invalid numeric values, and inconsistent date formats. Manual preparation can be time-consuming and may reduce the reliability of analysis.

### 3. Objectives
- Identify missing values and duplicate rows.
- Standardize text fields and date formats.
- Handle selected invalid numeric values.
- Fill missing numeric values using median values.
- Generate visual summaries and downloadable reports.

### 4. Technologies
Python, Pandas, NumPy, Matplotlib, Streamlit, and OpenPyXL.

### 5. Dataset
The supplied synthetic customer dataset contains customer ID, name, email, age, city, purchase amount, and join date. It intentionally includes missing values, extra spaces, mixed capitalization, a duplicate record, an invalid age, a negative amount, and mixed date formats.

### 6. Methodology
1. Load a CSV file or the sample dataset.
2. Inspect row counts, missing cells, and duplicate rows.
3. Convert blank text cells to missing values.
4. Trim spaces and standardize email and city values.
5. Optionally convert negative numeric values to missing values.
6. Treat ages above 100 as invalid when an Age column exists.
7. Optionally fill missing numeric values using column medians.
8. Parse columns containing `date` in their names.
9. Optionally remove exact duplicate rows.
10. Display previews, charts, descriptive statistics, and a cleaning summary.
11. Export cleaned CSV, summary CSV, and Excel workbook.

### 7. Expected output
Cleaned dataset preview, missing-value chart, numeric summary, before/after cleaning report, downloadable CSV and Excel files.

### 8. Conclusion
The project demonstrates how common data-quality tasks can be automated through Python. Cleaning rules should be reviewed against the meaning of the real dataset before using the output for decisions.

### 9. Future enhancements
Add custom column validation, PDF reports, outlier detection, scheduled reporting, and database connectivity.

### 10. References
- https://pandas.pydata.org/docs/
- https://numpy.org/doc/
- https://docs.streamlit.io/
- https://matplotlib.org/stable/
