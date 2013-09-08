__author__ = 'orhan'

from unittest import TestCase
from common.geometry import Point
from sys import float_info


class GeometryTests(TestCase):

    epsilon = 1e-6

    def test_point(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(0.0, 0.0)

        self.assertTrue(p1.angle_x(p2) - 45.0 <= self.epsilon)

    def test_point2(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(0.0, 0.0)

        self.assertTrue(p2.angle_x(p1) - 135.0 <= self.epsilon)

    def test_point3(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(1.0, 1.0)

        self.assertTrue(p2.angle_x(p1) - 0.0 <= self.epsilon)

    def test_point4(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(1.0, 0.0)

        self.assertTrue(p2.angle_x(p1) - 90.0 <= self.epsilon)

    def test_internals(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(0.0, 0.0)

        self.assertTrue(p1 != p2)
        self.assertTrue(not p1 == p2)

    def test_internals2(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(1.0, 0.0)

        self.assertTrue(p1 != p2)
        self.assertTrue(not p1 == p2)

    def test_internals3(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(1.0, 1.0)

        self.assertTrue(not p1 != p2)
        self.assertTrue(p1 == p2)

