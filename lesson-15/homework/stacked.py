import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

time_periods = ['T1', 'T2', 'T3', 'T4']

category_A = np.array([3, 5, 7, 6])
category_B = np.array([4, 6, 3, 5])
category_C = np.array([2, 4, 5, 7])

plt.bar(time_periods, category_A, label='Category A', color='blue')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='orange')
plt.bar(time_periods, category_C, bottom=category_A + category_B, label='Category C', color='green')

plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()

plt.show()
