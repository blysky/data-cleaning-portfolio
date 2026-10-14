import pandas as pd 
import numpy as np

#READ
df =  pd.read_csv('dirty_sales_data.csv')

#CLEAN
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
num_cols = df.select_dtypes(include= 'number').columns
obj_cols = df.select_dtypes(include= 'object').columns

for col in num_cols:
    df[col] = pd.to_numeric(df[col] , errors='coerce')

for col in obj_cols:
    df[col] = df[col].astype(str)


#DUPLICATES
df = df.drop_duplicates()

#PRICE
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df[df['price'] > 0]  
q1 = df['price'].quantile(0.25)
q3 = df['price'].quantile(0.75)
IQR = q3 - q1
upper_bound = q3 + 1.5 * IQR
clean_df = df[df['price'] < upper_bound]
clean_df['price'] = clean_df['price'].fillna(clean_df['price'].median())

#CITY
clean_df['city'] = clean_df['city'].fillna(method = 'ffill')

#DATE
clean_df = clean_df.dropna(subset=['order_date'])
clean_df['order_date'] = pd.to_datetime(clean_df['order_date'] , errors = 'coerce')
today = pd.Timestamp.today()
min_date = pd.Timestamp('2000-01-01')
clean_df = clean_df[(clean_df['order_date'] <= today) & (clean_df['order_date'] > min_date)]

#QUANTITY
clean_df = clean_df[clean_df['quantity'] > 0]

clean_df['total_price'] = clean_df['price'] * clean_df['quantity']

clean_df.to_csv('new_clean_sale.csv')