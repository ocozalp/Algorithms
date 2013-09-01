__author__ = 'orhan'

from unittest import TestCase
from unionfind.quickfind import QuickFind
from unionfind.quickunion import QuickUnion
from unionfind.weightedquickunion import WeightedQuickUnion
from unionfind.wquwithpathcompression import WQUWithPathCompression


class UnionFindTests():

    def test_initial(self):
        self.assertEqual(self.algorithm.parent(1), 1)

    def test_simple_connect(self):
        self.algorithm.connect(1, 2)
        self.assertTrue(self.algorithm.isConnected(1, 2))

    def test_multiple_connect(self):
        self.algorithm.connect(1, 2)
        self.algorithm.connect(3, 4)
        self.assertTrue(not self.algorithm.isConnected(2, 3))
        self.algorithm.connect(1, 4)
        self.assertTrue(self.algorithm.isConnected(2, 3))
        self.assertTrue(self.algorithm.isConnected(2, 4))
        self.assertTrue(not self.algorithm.isConnected(2, 9))


class QuickFindTests(UnionFindTests, TestCase):

    def setUp(self):
        self.algorithm = QuickFind(100)


class QuickUnionTests(UnionFindTests, TestCase):

    def setUp(self):
        self.algorithm = QuickUnion(100)


class WeightedQuickUnionTests(UnionFindTests, TestCase):

    def setUp(self):
        self.algorithm = WeightedQuickUnion(100)


class WQUWithPathCompressionTests(UnionFindTests, TestCase):

    def setUp(self):
        self.algorithm = WQUWithPathCompression(100)