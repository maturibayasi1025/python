import pandas as pd

xlsx = pd.read_excel("kadai.xlsx")

xlsx["data3"] = ["b","4","e","6","a","8"]

print(len(xlsx.index))
print(xlsx)
