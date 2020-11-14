from unittest import TestCase

from src.vec2 import Vec2


class Vec2PositiveTests(TestCase):
    """Test the Vec2 class for positive tests"""

    def test_create_vec2_positive(self):
        """Test successfully creating a Vec2 object"""
        x = -1
        y = 0.1

        v1 = Vec2(x, y)
        v2 = Vec2([x, y])
        v3 = Vec2((x, y))
        v4 = Vec2(str(x), str(y))

        self.assertEqual(v1.x, x)
        self.assertEqual(v1.y, y)

        self.assertEqual(v2, v1)
        self.assertEqual(v3, v1)
        self.assertEqual(v4, v1)

    def test_create_vec2_default_positive(self):
        """Test creating a vec2 with default parameters"""
        v1 = Vec2()
        v2 = Vec2(1)

        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)

        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 0)

    def test_operations_vec2_positive(self):
        """Test the basic operations involving a vec2 objects"""
        v1 = Vec2(-4, 3)
        v2 = Vec2(0.1, -2.5)

        self.assertTrue(Vec2(1.5, 2.0) == Vec2(1.5, 2))
        self.assertTrue(Vec2(1.5, 2.0) != Vec2(-1.5, 2))
        self.assertEqual(-v1, Vec2(4, -3))
        self.assertEqual(v1 + v2, Vec2(-3.9, 0.5))
        self.assertEqual(v1 - v2, Vec2(-4.1, 5.5))
        self.assertEqual(v2 - v1, Vec2(4.1, -5.5))
        self.assertEqual(3 * v1, Vec2(-12, 9))
        self.assertEqual(v1 * 3, Vec2(-12, 9))
        self.assertEqual(v1 / 2, Vec2(-2, 1.5))
        self.assertEqual(v1 // 2, Vec2(-2, 1))

        self.assertEqual(v1.dot(v2), -7.9)
        self.assertEqual(v2.dot(v1), -7.9)
        self.assertEqual(v1.norm(), 5)
        self.assertEqual(abs(v1), 5)
        self.assertEqual(v1.versor().norm(), 1)
        self.assertEqual(v1.versor() * v1.norm(), v1)


class Vec2NegativeTests(TestCase):
    """Test the Vec2 class for negative tests"""

    def test_create_vec2_negative(self):
        """Test trying to create illegal vec2 raises an error"""
        invalid_arguments = [
            ('a', ),
            (1, 'a'),
            (['b', 2], ),
            (('b', 2), ),
            ([1], ),
            ((1, ), ),
            ([1, 2, 3], ),
            ((1, 2, 3), ),
        ]

        for args in invalid_arguments:
            with self.assertRaises(ValueError):
                Vec2(*args)

    def test_operations_vec2_negative(self):
        """Test the basic operations involving a vec2 objects"""
        v1 = Vec2(-2, 3)
        v2 = Vec2(0.1, 2.5)

        with self.assertRaises(TypeError):
            v1 * v2

        with self.assertRaises(TypeError):
            1 / v1

        with self.assertRaises(TypeError):
            v2 / v1
