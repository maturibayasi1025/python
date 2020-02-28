import pandas as pd

# csvファイルの読みこみ
data = pd.read_csv(
    "https://aiacademy.jp/dataset/sample_data.csv",
    encoding="cp932",
    skiprows=1
)

print(data)
print(type(data))
print(data.dtypes)

"""
エクセルの場合は下記のように使う。
.read_excel("任意のファイル名.xlsx",encoding='utf8')
"""
