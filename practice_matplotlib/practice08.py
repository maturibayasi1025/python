import matplotlib.pyplot as plt

x1,y1 = range(0,5),[10,41,44,29,85]
x2,y2 = range(0,5),[59,55,77,15,47]

fig = plt.figure()

a1 = fig.add_subplot(1,2,1)
a1.bar(x1,y1)
a1.set_title("A")

a2 = fig.add_subplot(1,2,2)
a2.bar(x2,y2)
a2.set_title("B")

plt.show()
