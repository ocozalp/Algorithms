__author__ = 'orhan'

from unittest.case import TestCase
from convexhull.grahamscan import GrahamScan
from common.geometry import Point


class GeometryTests(TestCase):

    def test_1(self):
        gs = GrahamScan()
        gs.add_point(Point(0.0, 0.0))
        gs.add_point(Point(1.0, 0.0))
        gs.add_point(Point(1.0, 1.0))
        gs.add_point(Point(0.0, 1.0))

        res = gs.calculate()

        self.assertTrue(len(res) == 4)

    def test_2(self):
        gs = GrahamScan()
        gs.add_point(Point(0.0, 0.0))
        gs.add_point(Point(1.0, 0.0))
        gs.add_point(Point(1.0, 1.0))
        gs.add_point(Point(0.0, 1.0))

        p5 = Point(0.5, 0.5)
        gs.add_point(p5)

        res = gs.calculate()

        self.assertTrue(len(res) == 4)
        self.assertTrue(p5 not in res)

    def test_3(self):
        gs = GrahamScan()
        gs.add_point(Point(0.0, 0.0))
        gs.add_point(Point(5.0, 0.0))
        gs.add_point(Point(4.0, -1.0))
        gs.add_point(Point(4.0, 5.0))
        gs.add_point(Point(0.0, 5.0))

        p5 = Point(2.5, 2.5)
        gs.add_point(p5)

        p6 = Point(1.0, 1.0)
        gs.add_point(p6)

        res = gs.calculate()

        self.assertTrue(len(res) == 5)
        self.assertTrue(p5 not in res)
        self.assertTrue(p6 not in res)

    def test_4(self):
        gs = GrahamScan()
        gs.add_point(Point(0.0, 0.0))
        gs.add_point(Point(1.0, 1.0))
        gs.add_point(Point(2.0, 2.0))

        res = gs.calculate()

        self.assertTrue(len(res) == 3)