import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv('https://raw.githubusercontent.com/jennah1016/pandas-basics/refs/heads/main/electric%20billing%20data.csv')
df.plot(kind='box')

plt.title("Electric Billing Data Outliers")
plt.xlabel("Year")
plt.ylabel("Amount Spent (millions of dollars)")

plt.show()