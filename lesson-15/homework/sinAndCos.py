import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


x =  np.arange(0, 2*np.pi, 0.001)
y = np.sin(x)
plt.plot(x, y, 'r:', label='sin(x)')
# plt.scatter(x, y)
z = np.cos(x)
# plt.scatter(z, y)
plt.plot(x, z, 'b-', label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('trigonometric functions')
plt.grid(True, linestyle='--', linewidth=0.3)
plt.show()