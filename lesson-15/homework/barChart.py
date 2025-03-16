import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


data = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['b', 'g', 'r', 'c', 'm']

plt.bar(data, values, color=colors, width=0.9)
plt.xticks(np.arange(len(data)), data)
plt.title('Products')
plt.ylabel('Values')
plt.xlabel('smth')
plt.show()