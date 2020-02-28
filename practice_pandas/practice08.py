import pandas as pd
import numpy as np

df = pd.DataFrame({
    "int":[1,np.nan,np.nan,32],
    "str":["python","ai",np.nan,np.nan],
    "flt":[5.5,4.2,-1.2,np.nan]
})

#print(df)

"""
df成分に対してNaNの地位をTrueとしたプールの値のデータフレームを返す
"""
#print(df.isnull()) # notnull()を使うとTrueとFalseが逆になる

"""
NaNがある行を全て削除する
"""
#print(df.dropna())

"""
NaNを全て0に置き換える
"""
#print(df.fillna(0))

df2 = pd.DataFrame({
    "int":[1,np.nan,np.nan,32],
    "str":["python","ai",np.nan,np.nan],
    "flt":[5.5,4.2,-1.2,np.nan]
})

"""
int列だけ0に補完
"""
#print(df2.fillna({"int":0}))

"""
列ごとに異なる値を使いたい時は複数のキーを渡す。
"""
#print(df2.fillna({"int":0,"str":"ai"}))

"""
特定の列を削除
"""
#print(df2.drop(labels="flt",axis=1))

"""
複数の列を削除
"""
#print(df2.drop(labels=["flt","str"],axis=1))

"""
indexを指定することで行を消すこともできる
"""
#print(df2.drop(index=1,axis=0))

"""
元データに反映して削除するにはinplaceオプションにTrueを渡す。
"""
# df2.drop(labels="flt",axis=1,inplace=True)
# print(df2)

"""
ランダムに6行3列のデータを生成する
"""
df3 = pd.DataFrame(np.random.rand(6,3))
print(df3)

