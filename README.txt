# Data Cleaning Pipeline

Automated ETL pipeline for sales data validation and cleaning using pandas.

## Features
- Column standardization (lowercase, spacing, underscores)
- Type conversion (numeric, datetime, string)
- Duplicate removal
- Outlier detection (IQR method on price)
- Missing data imputation (median fill, forward fill)
- Data validation (positive values, date range checks)
- Computed fields (total_price = price × quantity)

## Usage
```python
python sales_pipeline.py
```

**Input:** `dirty_sales_data.csv`
**Output:** `new_clean_sales.csv`

## Skills Demonstrated
- pandas (data manipulation, type conversion, aggregation)
- NumPy (quantile calculations)
- Data quality validation
- ETL workflow design
