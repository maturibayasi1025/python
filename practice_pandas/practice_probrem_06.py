import pandas as pd

csv = pd.read_csv("kadai.csv")
print(csv)
print(type(csv))

xlsx = pd.read_excel("kadai.xlsx")
print(xlsx)
