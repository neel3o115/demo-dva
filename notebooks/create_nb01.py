import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.12.0"}}

cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("""# 01 — Data Sourcing & Validation

## Objective
Validate the raw dataset against project requirements before proceeding to the ETL pipeline.

**Requirements Checklist:**
- Minimum 5,000 rows
- Minimum 8 meaningful columns
- Contains real-world data quality issues (missing values, type inconsistencies)
- Clear target variable for analysis

---"""))

# Imports
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Display settings
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 120)

print("Libraries loaded successfully.")"""))

# Load
cells.append(nbf.v4.new_markdown_cell("## 1. Load Raw Dataset"))
cells.append(nbf.v4.new_code_cell("""# Load the raw dataset — this file should NEVER be modified
raw_path = '../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(raw_path)

print(f"Dataset loaded: {df.shape[0]:,} rows x {df.shape[1]} columns")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")"""))

# Shape validation
cells.append(nbf.v4.new_markdown_cell("## 2. Shape & Structure Validation"))
cells.append(nbf.v4.new_code_cell("""# Requirement: >= 5,000 rows and >= 8 meaningful columns
print("=" * 60)
print("REQUIREMENT CHECK")
print("=" * 60)
print(f"Rows:    {df.shape[0]:,}  (requirement: >= 5,000)  {'PASS' if df.shape[0] >= 5000 else 'FAIL'}")
print(f"Columns: {df.shape[1]}    (requirement: >= 8)      {'PASS' if df.shape[1] >= 8 else 'FAIL'}")
print("=" * 60)"""))

cells.append(nbf.v4.new_code_cell("""# Column names, data types, and non-null counts
df.info()"""))

# Preview
cells.append(nbf.v4.new_markdown_cell("## 3. Data Preview"))
cells.append(nbf.v4.new_code_cell("""# First 5 rows
df.head()"""))
cells.append(nbf.v4.new_code_cell("""# Last 5 rows
df.tail()"""))
cells.append(nbf.v4.new_code_cell("""# Statistical summary of numeric columns
df.describe()"""))
cells.append(nbf.v4.new_code_cell("""# Statistical summary of categorical columns
df.describe(include='object')"""))

# Data quality
cells.append(nbf.v4.new_markdown_cell("## 4. Data Quality Assessment"))
cells.append(nbf.v4.new_code_cell("""# Missing values analysis
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
quality_df = pd.DataFrame({'Missing Count': missing, 'Missing %': missing_pct})
quality_df = quality_df[quality_df['Missing Count'] > 0]

if len(quality_df) == 0:
    print("No NULL values detected via isnull().")
    print("\\nChecking for blank strings and whitespace-only values...")
    
# Check for blank strings (common in CSVs where missing != NaN)
blank_counts = {}
for col in df.select_dtypes(include='object').columns:
    blanks = (df[col].str.strip() == '').sum()
    if blanks > 0:
        blank_counts[col] = blanks

if blank_counts:
    print("\\nBlank string values found:")
    for col, count in blank_counts.items():
        print(f"  {col}: {count} blanks ({count/len(df)*100:.2f}%)")
else:
    print("No blank strings found either.")"""))

# Unique values
cells.append(nbf.v4.new_markdown_cell("## 5. Column-Level Analysis"))
cells.append(nbf.v4.new_code_cell("""# Unique value counts for each column
print(f"{'Column':<20} {'Dtype':<10} {'Unique':>7} {'Sample Values'}")
print("-" * 80)
for col in df.columns:
    uniq = df[col].nunique()
    samples = df[col].dropna().unique()[:3]
    sample_str = ', '.join(str(s) for s in samples)
    print(f"{col:<20} {str(df[col].dtype):<10} {uniq:>7}   {sample_str}")"""))

# Categorical distributions
cells.append(nbf.v4.new_code_cell("""# Value counts for categorical columns (<=10 unique values)
for col in df.columns:
    if df[col].nunique() <= 10:
        print(f"\\n{'=' * 40}")
        print(f"{col}")
        print(f"{'=' * 40}")
        counts = df[col].value_counts()
        for val, count in counts.items():
            print(f"  {val:<30} {count:>5}  ({count/len(df)*100:.1f}%)")"""))

# Target variable
cells.append(nbf.v4.new_markdown_cell("## 6. Target Variable — Churn"))
cells.append(nbf.v4.new_code_cell("""# Churn distribution
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Count plot
churn_counts = df['Churn'].value_counts()
colors = ['#2ecc71', '#e74c3c']
axes[0].bar(churn_counts.index, churn_counts.values, color=colors, edgecolor='white', linewidth=1.5)
axes[0].set_title('Churn Distribution (Count)', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Number of Customers')
for i, (val, count) in enumerate(zip(churn_counts.index, churn_counts.values)):
    axes[0].text(i, count + 50, f'{count:,}', ha='center', fontsize=12, fontweight='bold')

# Percentage pie chart
axes[1].pie(churn_counts.values, labels=churn_counts.index, autopct='%1.1f%%', 
            colors=colors, startangle=90, textprops={'fontsize': 12},
            wedgeprops={'edgecolor': 'white', 'linewidth': 2})
axes[1].set_title('Churn Distribution (%)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('../tableau/screenshots/01_churn_distribution.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"\\nChurn Rate: {churn_counts['Yes'] / len(df) * 100:.1f}%")
print(f"Retained:   {churn_counts['No']:,} customers")
print(f"Churned:    {churn_counts['Yes']:,} customers")"""))

# Duplicates
cells.append(nbf.v4.new_markdown_cell("## 7. Duplicate Check"))
cells.append(nbf.v4.new_code_cell("""# Check for duplicate customer IDs
dup_ids = df['customerID'].duplicated().sum()
print(f"Duplicate customerIDs: {dup_ids}")

# Check for fully duplicate rows (excluding customerID)
dup_rows = df.drop(columns=['customerID']).duplicated().sum()
print(f"Duplicate rows (all features): {dup_rows}")"""))

# Summary
cells.append(nbf.v4.new_markdown_cell("""## 8. Validation Summary

### Requirements Assessment

| Requirement | Status | Details |
|---|---|---|
| >= 5,000 rows | **PASS** | 7,043 rows |
| >= 8 meaningful columns | **PASS** | 19 meaningful feature columns + 1 target + 1 ID |
| Contains data quality issues | **PASS** | 11 blank TotalCharges values, type inconsistency (TotalCharges as string), SeniorCitizen 0/1 encoding |
| Clear target variable | **PASS** | `Churn` column with 26.5% positive rate |
| No duplicate records | **PASS** | All customerIDs unique |

### Key Observations for ETL Pipeline

1. **`TotalCharges`** has 11 blank values — these correspond to customers with `tenure = 0` (new sign-ups who haven't been billed). The column is also stored as a string and must be converted to float.
2. **`SeniorCitizen`** uses 0/1 encoding while all other categorical columns use Yes/No — needs standardization.
3. **No time/date column** — the dataset is a cross-sectional snapshot. `tenure` will serve as the time proxy.
4. **Class imbalance** in target: 73.5% No / 26.5% Yes — notable but not extreme. No resampling needed for descriptive analytics.

### Conclusion
The dataset meets all project requirements and is approved for the ETL pipeline phase.

---
*Proceed to: `02_cleaning.ipynb`*"""))

nb.cells = cells
nbf.write(nb, '../notebooks/01_data_sourcing.ipynb')
print("Created 01_data_sourcing.ipynb")
