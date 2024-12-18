import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/jennah1016/pandas-basics/refs/heads/main/electric%20billing%20data.csv')

df.plot()

#add labels to the graph
plt.title("CTA Electric Billing Data: January 2022 - September 2024")
plt.xlabel("month")
plt.ylabel("amount spent (millions)")

#display graph
plt.show()

