import pandas as pd

xlsx = pd.read_excel("kadai.xlsx")

xlsx["data3"] = ["b","4","e","6","a","8"]

s = pd.Series(["c",12,"b",78],index = xlsx.columns)
print(s)

xlsx = xlsx.append(s,ignore_index=True)
print(xlsx)
