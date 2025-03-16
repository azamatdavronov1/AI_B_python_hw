import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 1)
y = x**2 + 4*x + 1

plt.plot(x, y, 'b-')
plt.scatter(x, y, marker="*")

plt.show()
