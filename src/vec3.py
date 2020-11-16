import math

from .vec2 import Vec2


class Vec3:
    """Represent a vector with 3 coordinates"""

    def __init__(self, x=0, y=0, z=0):
        if type(x) is list or type(x) is tuple:
            try:
                assert len(x) == 3
                self._create(*x)
            except AssertionError:
                raise ValueError('Vec3 must have exactly 3 components!')
        elif type(x) is Vec2:
            self._create(x.x, x.y, 0)
        else:
            self._create(x, y, z)

    def _create(self, x, y, z):
        try:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        except (ValueError, TypeError) as e:
            raise ValueError('Vector components must be float convertable!') \
                from e

    def __str__(self):
        return f'Vec3({self.x}, {self.y}, {self.z})'

    __repr__ = __str__

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other):
        """Add two Vec3 obejcts"""
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Subtract two Vec3 obejcts"""
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """Multiply the vector with a scalar"""
        if type(scalar) is not int and type(scalar) is not float:
            raise TypeError('Only scalar multiplication allow for Vec3')
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        """Divide the vector by a scalar"""
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __floordiv__(self, scalar):
        """Divide and floor the vector by a scalar"""
        return Vec3(self.x // scalar, self.y // scalar, self.z // scalar)

    def dot(self, other):
        """Return the dot product with another Vec3"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def norm(self):
        """Return the norm of the vector"""
        return math.sqrt(self.dot(self))

    __abs__ = norm

    def versor(self):
        """Return the normalized vec3"""
        return self / self.norm()
