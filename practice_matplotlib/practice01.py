import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-5,5,0.1) # -5から5まで0.1区切りで配列を作る
Y = np.sin(X) # 配列Xの値に関してそれぞれsin(X)を求めて、Y軸の配列を生成

plt.plot(X,Y) # この場合のplot関数の第一引数Xは、X軸に対応し、第二引数のYがY軸に当たる。
