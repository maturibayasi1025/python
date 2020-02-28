import matplotlib.pyplot as plt
import numpy as np

# 平均10、標準偏差10の正規乱数を100件生成
x = np.random.normal(10,10,1000)

plt.hist(x)

plt.show()
