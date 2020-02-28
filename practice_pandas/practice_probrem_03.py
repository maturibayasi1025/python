import pandas as pd

url = 'https://aiacademy.jp/dataset/sns_data.csv'

df = pd.read_csv(
    url,
    encoding="cp932",
    skiprows=1
)

df.columns = ["user_id","follow","follower","like"]
df.to_csv('output.csv',index=False)
