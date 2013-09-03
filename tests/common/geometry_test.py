__author__ = 'orhan'

from unittest import TestCase
from common.geometry import Point
from sys import float_info


class GeometryTests(TestCase):

    def test_point(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(0.0, 0.0)

        self.assertTrue(p1.angleX(p2) - 45.0 <= float_info.epsilon)

    def test_point2(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(0.0, 0.0)

        self.assertTrue(p2.angleX(p1) - 135.0 <= float_info.epsilon)

    def test_point3(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(1.0, 1.0)

        self.assertTrue(p2.angleX(p1) - 0.0 <= float_info.epsilon)

    def test_point4(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(1.0, 0.0)

        self.assertTrue(p2.angleX(p1) - 90.0 <= float_info.epsilon)
