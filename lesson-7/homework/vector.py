
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
        return sum(x ** 2 for x in self.val)**0.5
    
    def normalize(self):
        m = self.magnitude()
        if m == 0:
            raise ValueError("Zero vector cannot be normalized!")
        return Vector(*[x / m for x in self.val])

