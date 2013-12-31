from unittest.case import TestCase
from string_algorithms.search.robin_karp import robin_karp


class RobinKarpTests(TestCase):

    def get_strings(self):
        return "abcdabcdabcdabcdabcdabcdabcdabcd", "bcd"

    def test_search1(self):
        text, pattern = self.get_strings()

        ind = robin_karp(text, pattern)
        self.assertTrue(ind == 1)

    def test_search2(self):
        text, pattern = self.get_strings()

        ind = robin_karp(text, pattern, 2)
        self.assertTrue(ind == 5)

    def test_search3(self):
        text, pattern = self.get_strings()

        ind = robin_karp(text, pattern, len(text) - 1)
        self.assertTrue(ind == -1)

    def test_search4(self):
        text, pattern = self.get_strings()

        ind = robin_karp(text, pattern, len(text) + 1)
        self.assertTrue(ind == -1)