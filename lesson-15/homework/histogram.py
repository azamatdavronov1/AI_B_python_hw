import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.hist(data, bins=50, color='r', edgecolor='white', alpha=0.7)
plt.show()



