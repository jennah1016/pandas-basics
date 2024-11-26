import pandas as pd
df = pd.read_csv('electric billing data.csv')

avg2022 = df["2022"].mean()
avg2023 = df['2023'].mean()
avg2024YTD = df['2024 YTD'].mean()

#to-do: round float values to 2 decimal places
print('CTA electric billing data: January 2022 - September 2024:\n')
print (df.to_string())

print(f'\n2022 average : ${avg2022:.2f}')
print(f'2023 average: ${avg2023:.2f}')
print(f'2024 YTD average: ${avg2024YTD:.2f}')