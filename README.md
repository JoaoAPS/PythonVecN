# PythonVectors

Implementation of a Vec2 and Vec3 classes, useful for representation of vectors or
points in 2D and 3D space.

### Usage

``` python
from vecN import Vec2
from vecN import Vec3

v2 = Vec2(1, 2)
v3 = Vec3(1, 2, 3)

v2 + Vec2(2, 4)
# -> Vec2(3.0, 6.0)

2 * v3
# -> Vec3(2.0, 4.0, 6.0)

v2.norm()
# -> 2.23606797749979

v2.dot(Vec2(1, 1))
# -> 3.0

v2.versor()
# -> Vec2(0.4472135954999579, 0.8944271909999159)

v2.versor.norm()
# -> 1.0
```
