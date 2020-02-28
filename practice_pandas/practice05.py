import pandas as pd

df = pd.DataFrame(
    [[10,20,30,30],[25,50,65,80]],
    index=["1行","2行"],
    columns=["A","B","C","D"]
)

#単純表示
#print(df)

# 条件抽出
print(df.query('A >= 25 and C <= 70'))