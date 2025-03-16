import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

colors = np.random.rand(100)
sizes = np.random.randint(20, 100, 100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label="Color Scale")
plt.grid(visible=True)
plt.show()