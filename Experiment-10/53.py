import pandas as pd

df = pd.read_excel('abc.xlsx')

print("Sum: ",df["Production"].sum()) 
print("Mean: ",df["Production"].mean())
print("Maximum: ",df["Production"].max())
print("Minimum: ",df["Production"].min()) 