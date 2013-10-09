from unittest import TestCase
from common.data_structures import Node
from search.uninformed_search import bfs, dfs, iterative_deepening_search


class UninformedSearchTest(object):

    @staticmethod
    def prepare_tree1():
        node = Node()
        node.value = '1'

        node2 = Node()
        node2.value = '2'
        node.add_child(node2)
        node2 = Node()
        node2.value = '3'
        node.add_child(node2)
        node3 = Node()
        node3.value = '4'
        node2.add_child(node3)
        node3 = Node()
        node3.value = '5'
        node2.add_child(node3)

        return node

    @staticmethod
    def prepare_single_node_tree():
        node = Node()
        node.value = '1'

        return node

    @staticmethod
    def prepare_graph1():
        node = Node()
        node.value = '1'

        node2 = Node()
        node2.value = '2'
        node.add_child(node2)
        node21 = Node()
        node21.value = '3'
        node.add_child(node21)

        node3 = Node()
        node3.value = '4'
        node2.add_child(node3)

        node4 = Node()
        node4.value = '5'
        node3.add_child(node4)
        node21.add_child(node4)

        node5 = Node()
        node5.value = '6'
        node3.add_child(node5)

        return node

    def test_tree1(self):
        node = UninformedSearchTest.prepare_tree1()
        result = self.algorithm(node, '5')
        self.assertTrue(result.value == '5')

    def test_tree2(self):
        node = UninformedSearchTest.prepare_tree1()
        result = self.algorithm(node, '7')
        self.assertTrue(result is None)

    def test_tree3(self):
        node = UninformedSearchTest.prepare_single_node_tree()
        result = self.algorithm(node, '1')
        self.assertTrue(result.value == '1')

    def test_tree4(self):
        node = UninformedSearchTest.prepare_single_node_tree()
        result = self.algorithm(node, '2')
        self.assertTrue(result is None)

    def test_tree_with_comparator1(self):
        node = UninformedSearchTest.prepare_tree1()
        result = self.algorithm(node, 5, comparator=lambda x, y: int(x) == y)
        self.assertTrue(result.value == '5')

    def test_graph1(self):
        node = UninformedSearchTest.prepare_graph1()
        result = self.algorithm(node, '1')
        self.assertTrue(result.value == '1')

    def test_graph2(self):
        node = UninformedSearchTest.prepare_graph1()
        result = self.algorithm(node, '10')
        self.assertTrue(result is None)

    def test_graph3(self):
        node = UninformedSearchTest.prepare_graph1()
        result = self.algorithm(node, '5')
        self.assertTrue(result.value == '5')

    def test_graph4(self):
        node = UninformedSearchTest.prepare_graph1()
        result = self.algorithm(node, '6')
        self.assertTrue(result.value == '6')


class BfsTest(UninformedSearchTest, TestCase):

    def setUp(self):
        self.algorithm = bfs


class DfsTest(UninformedSearchTest, TestCase):

    def setUp(self):
        self.algorithm = dfs


class IterativeDeepeningSearch(UninformedSearchTest, TestCase):

    def setUp(self):
        self.algorithm = iterative_deepening_search