import matplotlib.pyplot as plt
import numpy as np

# 数学の点数
math = [20, 59, 81, 63, 96, 78, 54, 49, 66, 30]
# 英語の点数
english = [77, 92, 62, 77, 64, 45, 28, 60, 37, 86]

# 点数のタプル
points = (math,english)

# 箱ひげ図
fig,ax = plt.subplots()

bp = ax.boxplot(points) #複数指定する場合はタプル型で渡す
ax.set_xticklabels(['math','english'])

plt.title('exam')
plt.grid()
plt.show()

# x = np.array(math)
# plt.title("height")
# plt.grid() #横線ラインを入れることが可能

# plt.boxplot(x)
# plt.show()
