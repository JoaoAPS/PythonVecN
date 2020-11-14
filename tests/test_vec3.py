from unittest import TestCase

from src.vec3 import Vec3


class Vec3PositiveTests(TestCase):
    """Test the Vec3 class for successful operations"""

    def test_create_vec3_positive(self):
        """Test successfully creating a Vec3 object"""
        x = -1
        y = 0
        z = 1.4

        v1 = Vec3(x, y, z)
        v2 = Vec3([x, y, z])
        v3 = Vec3((x, y, z))
        v4 = Vec3(str(x), str(y), str(z))

        self.assertEqual(v1.x, x)
        self.assertEqual(v1.y, y)
        self.assertEqual(v1.z, z)

        self.assertEqual(v2, v1)
        self.assertEqual(v3, v1)
        self.assertEqual(v4, v1)

    def test_create_vec3_default_positive(self):
        """Test creating a vec3 with default parameters"""
        v1 = Vec3()
        v2 = Vec3(1)

        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)
        self.assertEqual(v1.z, 0)

        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 0)
        self.assertEqual(v2.z, 0)

    def test_operators_vec3_positive(self):
        """Test operators involving a vec3 objects in successful cases"""
        v1 = Vec3(-2, 3, 6)
        v2 = Vec3(0.1, -2.5, 0)

        self.assertTrue(Vec3(1.5, 2.0, 3) == Vec3(1.5, 2, 3))
        self.assertTrue(Vec3(1.5, 2.0, 3) != Vec3(-1.5, 2, 3))

        self.assertEqual(-v1, Vec3(2, -3, -6))
        self.assertEqual(v1 + v2, Vec3(-1.9, 0.5, 6))
        self.assertEqual(v1 - v2, Vec3(-2.1, 5.5, 6))
        self.assertEqual(v2 - v1, Vec3(2.1, -5.5, -6))
        self.assertEqual(3 * v1, Vec3(-6, 9, 18))
        self.assertEqual(v1 * 3, Vec3(-6, 9, 18))
        self.assertEqual(v1 / 2, Vec3(-1, 1.5, 3))
        self.assertEqual(v1 // 2, Vec3(-1, 1, 3))

        self.assertEqual(v1.dot(v2), -7.7)
        self.assertEqual(v2.dot(v1), -7.7)
        self.assertEqual(v1.norm(), 7)
        self.assertEqual(abs(v1), 7)
        self.assertTrue(v1.versor().norm() - 1 < 1e-12)
        self.assertEqual(v1.versor() * v1.norm(), v1)


class Vec3NegativeTests(TestCase):
    """Test the Vec3 class for unsuccessful operations"""

    def test_create_vec3_negative(self):
        """Test trying to create illegal vec3 raises an error"""
        invalid_arguments = [
            ('a', ),
            (1, 2, 'a'),
            (['b', 2, 2], ),
            (('b', 2, 2), ),
            ([1, 2], ),
            ((1, 2), ),
            ([1, 2, 4, 5], ),
            ((1, 2, 4, 5), ),
        ]

        for args in invalid_arguments:
            with self.assertRaises(ValueError):
                Vec3(*args)

    def test_operators_vec3_negative(self):
        """Test operators involving a vec3 objects in unsuccessful cases"""
        v1 = Vec3(-2, 3, 6)
        v2 = Vec3(0.1, -2.5, 0)

        with self.assertRaises(TypeError):
            v1 * v2

        with self.assertRaises(TypeError):
            1 / v1

        with self.assertRaises(TypeError):
            v2 / v1
