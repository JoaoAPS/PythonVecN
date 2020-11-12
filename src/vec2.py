import math


class Vec2:
    """Represent a vector with 2 coordinates"""

    def __init__(self, x=0, y=0):
        if type(x) is list or tuple:
            try:
                assert len(x) == 2
                self._init(*x)
            except AssertionError:
                raise ValueError('Vec2 must have exactly 2 components!')
        self._create(x, y)

    def _create(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            raise ValueError('Vector components must be float convertable!')

    def __str__(self):
        return f'Vec2({self.x}, {self.y})'

    __repr__ = __str__

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __add__(self, other):
        """Add two Vec2 obejcts"""
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two Vec2 obejcts"""
        return Vec2(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Multiply the vector with a scalar"""
        return Vec2(scalar * self.x, scalar * self.y)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        """Divide the vector by a scalar"""
        return Vec2(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        """Divide and floor the vector by a scalar"""
        return Vec2(self.x // scalar, self.y // scalar)

    def dot(self, other):
        """Return the dot product with another Vec2"""
        return self.x * other.x + self.y * other.y

    def norm(self):
        """Return the norm of the vector"""
        return math.sqrt(self.dot(self))

    def versor(self):
        """Return the normalized vec2"""
        return self / self.norm()
