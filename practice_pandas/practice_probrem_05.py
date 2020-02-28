import pandas as pd

d1 = {"data1": ["a","b","c","d","c","a"], "data2": range(6)}

df1 = pd.DataFrame(d1)

df1.to_csv("kadai.csv")
df1.to_excel("kadai.xlsx",encoding="utf8")
