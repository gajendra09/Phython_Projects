import matplotlib.pyplot as plt
import numpy as np
xpnt = np.array([0, 6])
ypnt = np.array([0, 250])
plt.plot(xpnt, ypnt)
plt.show()

plt.plot(xpnt, ypnt, "o")
plt.show()

plt.plot(ypnt, marker="o")
plt.show()

plt.plot(ypnt, "o:r")
plt.show()

plt.plot(ypnt, marker="o", ms=20)
plt.show()

plt.plot(ypnt, marker="o", ms=20, mec='r')
plt.show()

plt.plot(ypnt, marker="o", ms=20, mfc='r')
plt.show()

plt.plot(ypnt, linestyle='dotted')
plt.show()

plt.plot(ypnt, color='r')
plt.show()

plt.plot(ypnt, linewidth='20')
plt.show()

plt.plot(xpnt)
plt.plot(ypnt)
plt.show()

plt.plot(xpnt, ypnt)
plt.title("test map")
plt.xlabel("x points")
plt.ylabel("Y points")
plt.show()

plt.plot(xpnt, ypnt)
plt.grid()
plt.show()

plt.plot(xpnt, ypnt)
plt.grid(axis='x')
plt.show()
