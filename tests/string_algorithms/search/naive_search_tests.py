from unittest.case import TestCase
from string_algorithms.search.naive_search import naive_search


class NaiveSearchTests(TestCase):

    def get_strings(self):
        return "abcdabcdabcdabcdabcdabcdabcdabcd", "bcd"

    def test_search1(self):
        text, pattern = self.get_strings()

        ind = naive_search(text, pattern)
        self.assertTrue(ind == 1)

    def test_search2(self):
        text, pattern = self.get_strings()

        ind = naive_search(text, pattern, 2)
        self.assertTrue(ind == 5)

    def test_search3(self):
        text, pattern = self.get_strings()

        ind = naive_search(text, pattern, len(text) - 1)
        self.assertTrue(ind == -1)

    def test_search4(self):
        text, pattern = self.get_strings()

        ind = naive_search(text, pattern, len(text) + 1)
        self.assertTrue(ind == -1)