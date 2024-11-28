import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/jennah1016/pandas-basics/refs/heads/main/electric%20billing%20data.csv')

#average spending for each year
avg2022 = df["2022"].mean()
avg2023 = df['2023'].mean()
avg2024YTD = df['2024 YTD'].mean()

#displays monthly billing totals
print('CTA electric billing data: January 2022 - September 2024:\n')
print (df.to_string())

#display average billing totals from each year
print(f'\n2022 average : ${avg2022:.2f}')
print(f'2023 average: ${avg2023:.2f}')
print(f'2024 YTD average: ${avg2024YTD:.2f}')

#to-do: learn how to find projected spending
'''octavg
novavg
decavg'''
