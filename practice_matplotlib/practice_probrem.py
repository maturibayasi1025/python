import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5,0.1)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.sin(-1 * x)

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.show()
