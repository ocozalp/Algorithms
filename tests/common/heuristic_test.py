from unittest import TestCase
from common.heuristic import euclidean, chebyshev, manhattan


class HeuristicTest(TestCase):

    def test_euclidean1(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 1, 2]

        self.assertTrue(euclidean(v1, v2) == 0.0)

    def test_euclidean2(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 5, 5]

        self.assertTrue(euclidean(v1, v2) == 5.0)

    def test_euclidean3(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 1]

        try:
            euclidean(v1, v2)
            self.assertTrue(False)
        except AssertionError as ae:
            self.assertTrue(True)

    def test_chebyshev1(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 1, 2]

        self.assertTrue(chebyshev(v1, v2) == 0.0)

    def test_chebyshev2(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 5, 5]

        self.assertTrue(chebyshev(v1, v2) == 4.0)

    def test_chebyshev3(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 1]

        try:
            chebyshev(v1, v2)
            self.assertTrue(False)
        except AssertionError as ae:
            self.assertTrue(True)

    def test_manhattan1(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 1, 2]

        self.assertTrue(manhattan(v1, v2) == 0.0)

    def test_manhattan2(self):
        v1 = [0, 1, 1, 2]
        v2 = [-1, 3, 4, 4]

        self.assertTrue(manhattan(v1, v2) == 8.0)

    def test_manhattan3(self):
        v1 = [0, 1, 1, 2]
        v2 = [0, 1, 1]

        try:
            manhattan(v1, v2)
            self.assertTrue(False)
        except AssertionError as ae:
            self.assertTrue(True)