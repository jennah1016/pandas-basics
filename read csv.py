import pandas as pd
df = pd.read_csv('electric billing data.csv')

avg2022 = df["2022"].mean()
avg2023 = df['2023'].mean()
avg2024YTD = df['2024 YTD'].mean()

print('CTA electric billing data: January 2022 - September 2024:\n')
#df['2024 YTD'].fillna('No Data', inplace=True)
print (df.to_string())

#to do: figure out how to concatenate numbers and strings
'''print('\n 2022 Average: ' + avg2022 + '\n')
print('2023 average: ' + avg2023 + '\n')
print('2024 average: ' + avg2024YTD + '\n')'''
