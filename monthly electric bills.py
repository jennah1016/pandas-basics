import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('electric billing data.csv')

df.plot()

plt.title("CTA Electric Billing Data: January 2022 - September 2024")
plt.xlabel("month")
plt.ylabel("amount spent (millions)")

plt.show()

