class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):  # Scalar product
            return Vector(*(a * other for a in self.components))
        return sum(a * b for a, b in zip(self.components, other.components))  # Dot product

    def __repr__(self):
        return f"Vector{self.components}"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)
print(v2 - v1)


