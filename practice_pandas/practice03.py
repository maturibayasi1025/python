import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20,2))
#print(df.head()) #先頭から5件
#print(df.tail()) #末尾から5件

print(df.head().append(df.tail())) #先頭から5件と末尾から5件の計10件分のデータを抽出
print(df.head(3).append(df.tail(3))) #先頭から3件と末尾から3件の計6件のデータを抽出
