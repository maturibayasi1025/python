import numpy as np

"""
配列生成 arange()
"""

# 0 ~ 9までの数字（配列）を生成。
x = np.arange(10)
print(x)

# reshape()は配列を指定された形状に変換します。
x = np.arange(1,10).reshape(3,3) # 3×3の多次元配列に変換される。
y = np.arange(1,10).reshape(3,3)

# 3×3の多次元配列が出力される。
print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)
