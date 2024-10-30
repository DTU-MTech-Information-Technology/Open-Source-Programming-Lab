import pandas as pd

df = pd.read_excel("./abc.xlsx", usecols=[1, 4])
print(df.head())
