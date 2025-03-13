import numpy as np


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


temps_f = np.array([32, 68, 100, 212, 77], dtype = int)
temps_c = np.vectorize(fahrenheit_to_celsius)(temps_f)
print("Temperatures in Celsius:", temps_c)
