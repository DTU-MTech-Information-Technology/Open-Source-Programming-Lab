import pandas as pd

df = pd.read_excel('abc.xlsx')

print("Sum: ",df["Marks"].sum()) 
print("Mean: ",df["Marks"].mean())
print("Maximum: ",df["Marks"].max())
print("Minimum: ",df["Marks"].min()) 