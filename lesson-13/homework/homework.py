import numpy as np

#1
vector = np.arange(10, 50)
print(vector)

#2
matrix = np.arange(9).reshape(3, 3)
print(matrix)

#3
identity = np.eye(3)
print(identity)

#4
cube = np.random.random((3, 3, 3))
print(cube)

#5
big_matrix = np.random.random((10, 10))
print("Min:", big_matrix.min(), "Max:", big_matrix.max())

#6
random_numbers = np.random.random(30)
print("Mean:", random_numbers.mean())

#7
matrix = np.random.random((5, 5))
normalized = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print(normalized)

#8
A = np.random.random((5, 3))
B = np.random.random((3, 2))
result = np.dot(A, B)
print(result)

#9
A = np.random.random((3, 3))
B = np.random.random((3, 3))
result = np.dot(A, B)
print(result)

#10
matrix = np.random.random((4, 4))
print(matrix.T)

#11
matrix = np.random.random((3, 3))
print("Determinant:", np.linalg.det(matrix))

#12
A = np.random.random((3, 4))
B = np.random.random((4, 3))
print(np.dot(A, B))

#13
matrix = np.random.random((3, 3))
vector = np.random.random((3, 1))
print(np.dot(matrix, vector))

#14
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print(x)

#15
matrix = np.random.random((5, 5))
print("Row sums:", matrix.sum(axis=1))
print("Column sums:", matrix.sum(axis=0))
