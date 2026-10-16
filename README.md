# Data cleaning pipeline

A pandas script that cleans a sales dataset with the usual problems: messy column
names, numbers stored as text, duplicate rows, outliers, and missing values. The
input is a 100-row CSV that I generated with AI to get realistic dirty data. I'd
rather say that plainly than have the data look more real than it is.

`sales_pipeline.py` reads `dirty_sales_data.csv`, runs these steps in order, and
writes `new_clean_sale.csv`:

standardises column names (strip spaces, lowercase, underscores)
converts numeric columns and drops prices of zero or less
removes duplicate rows
removes price outliers with the IQR rule, then fills missing prices with the median
fills missing cities from the row above
drops rows with dates outside 2000 to today, and rows with a quantity of zero or less
adds a `total_price` column (price × quantity)

To run it:

```
pip install pandas numpy
python sales_pipeline.py
```

Known issues: the script still raises pandas warnings about chained assignment and
the old `fillna(method=...)` call. The output is what I expected, but I haven't
cleaned up the code yet.