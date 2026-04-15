# Telco Customer Churn Analysis

## Project Overview

This project is an end-to-end data analytics capstone that investigates customer churn patterns in a telecommunications company. Using a dataset of 7,043 customer records across 21 attributes, we identify the key drivers of churn and deliver actionable retention strategies backed by statistical evidence.

## Problem Statement

> "What customer demographics, service subscriptions, and account attributes drive customer churn in a telecommunications company, and what targeted retention strategies can reduce the churn rate while maximizing customer lifetime value?"

## Sector

Telecommunications

## Dataset

- **Source:** IBM Watson Analytics Sample Dataset — Telco Customer Churn
- **Size:** 7,043 rows x 21 columns
- **Key Target Variable:** `Churn` (Yes/No)
- **Features:** Demographics (gender, senior citizen, partner, dependents), Services (phone, internet, add-ons), Account (contract, billing, payment method), Financials (monthly charges, total charges, tenure)

## Project Structure

```
├── data/
│   ├── raw/                          # Original, unedited dataset
│   └── processed/                    # Cleaned output after ETL
├── notebooks/
│   ├── 01_data_sourcing.ipynb        # Dataset exploration & validation
│   ├── 02_cleaning.ipynb             # Full ETL pipeline
│   ├── 03_eda.ipynb                  # Exploratory Data Analysis
│   ├── 04_statistical_analysis.ipynb # Statistical methods
│   └── 05_final_load_prep.ipynb      # KPIs & Tableau-ready data
├── tableau/
│   ├── screenshots/                  # Dashboard screenshots
│   └── dashboard_links.md           # Tableau Public URL
├── docs/
│   └── data_dictionary.md           # Column-by-column definitions
├── reports/
│   ├── final_report.pdf             # 10-15 page report
│   └── presentation.pdf            # Presentation deck
├── README.md
└── .gitignore
```

## How to Run

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn missingno
```

### Execution Order

1. `01_data_sourcing.ipynb` — Validates the raw dataset
2. `02_cleaning.ipynb` — Runs the ETL pipeline, outputs cleaned data to `data/processed/`
3. `03_eda.ipynb` — Exploratory analysis with visualizations
4. `04_statistical_analysis.ipynb` — Statistical tests and modeling
5. `05_final_load_prep.ipynb` — KPI computation and Tableau data export

Run each notebook sequentially. Each notebook documents its inputs and outputs.

## Key Findings

*(To be updated after analysis is complete)*

## Tableau Dashboard

Link: *(To be added after publishing to Tableau Public)*

## Team

| Name | Role |
|---|---|
| Member 1 | *Aayush Chaturvedi* |
| Member 2 | *Bhavya Jain* |
| Member 3 | *Dhruv Sareen* |
| Member 4 | *Jeevan BR* |
| Member 5 | *Neel Verma* |

## License

This project is for academic purposes as part of the DVA Capstone 2 coursework.
