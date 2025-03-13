import numpy as np


def power(num, power):
    return num ** power


numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])
results = np.vectorize(power)(numbers, powers)
print("Results:", results)

