from unittest.case import TestCase
from search.binary_search import binary_search


class BinarySearchTest(TestCase):

    def generate_array(self):
        return [1, 2, 12, 16, 25, 33, 57]

    def test_exists1(self):
        array = self.generate_array()
        ind = binary_search(array, 12)

        self.assertTrue(ind == 2)

    def test_exists2(self):
        array = self.generate_array()
        ind = binary_search(array, 1)

        self.assertTrue(ind == 0)

    def test_exists3(self):
        array = self.generate_array()
        ind = binary_search(array, 57)

        self.assertTrue(ind == 6)

    def test_not_exist1(self):
        array = self.generate_array()
        ind = binary_search(array, 3)

        self.assertTrue(ind == 2)

    def test_not_exist2(self):
        array = self.generate_array()
        ind = binary_search(array, 0)

        self.assertTrue(ind == 0)

    def test_not_exist3(self):
        array = self.generate_array()
        ind = binary_search(array, 60)

        self.assertTrue(ind == 7)

    def test_not_exist4(self):
        array = self.generate_array()
        ind = binary_search(array, 17)

        self.assertTrue(ind == 4)