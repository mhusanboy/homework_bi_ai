import math

class Vector:
        
    def __init__(self, *args):
        self.val = args

    def __str__(self):
        return f"Vector({', '.join(str(i) for i in self.val)})"

    def __add__(self, other):
        if len(self.val) != len(other.val):
            raise ValueError("Dimension of the instances is not compatible")
        
        return Vector(*[x + y for x, y in zip(self.val, other.val)])
    
    def __sub__(self, other):
        if len(self.val) != len(other.val):
            raise ValueError("Dimension of the instances is not compatible")
        
        return Vector(*[x - y for x, y in zip(self.val, other.val)])
    
    def dot(self, other):
        if len(self.val) != len(other.val):
            raise ValueError("Dimension of the instances is not compatible")
        
        return sum(sum(x * y for x, y in zip(self.val, other.val)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(x * other for x in self.val))
        
        if isinstance(other, Vector):
            if len(self.val) != len(other.val):
                raise ValueError("Dimension of the instances is not compatible")
        
            return Vector(*[x * y for x, y in zip(self.val, other.val)])

        raise TypeError(f"Unsupported operand type for *: 'Vector' and {type(other)}")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.val))
    
    def normalize(self):
        m = self.magnitude()
        return Vector(*[x / m for x in self.val])
    
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)