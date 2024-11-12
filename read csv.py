import pandas as pd
df = pd.read_csv('electric billing data.csv')
df['2024 YTD'].fillna('No Data', inplace=True)
print (df)