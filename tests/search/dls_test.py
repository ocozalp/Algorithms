from unittest.case import TestCase
from common.data_structures import Node
from search.uninformed_search import dls


class DepthLimitedSearchTest(TestCase):

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
        node = DepthLimitedSearchTest.prepare_tree1()
        result = dls(node, '5', 10)
        self.assertTrue(result.value == '5')

    def test_tree6(self):
        node = DepthLimitedSearchTest.prepare_tree1()
        result = dls(node, '5', 1)
        self.assertTrue(result is None)

    def test_tree2(self):
        node = DepthLimitedSearchTest.prepare_tree1()
        result = dls(node, '7', 10)
        self.assertTrue(result is None)

    def test_tree3(self):
        node = DepthLimitedSearchTest.prepare_single_node_tree()
        result = dls(node, '1', 0)
        self.assertTrue(result.value == '1')

    def test_tree4(self):
        node = DepthLimitedSearchTest.prepare_single_node_tree()
        result = dls(node, '2', 1)
        self.assertTrue(result is None)

    def test_tree5(self):
        node = DepthLimitedSearchTest.prepare_single_node_tree()
        result = dls(node, '2', 0)
        self.assertTrue(result is None)

    def test_tree_with_comparator1(self):
        node = DepthLimitedSearchTest.prepare_tree1()
        result = dls(node, 5, 5, comparator=lambda x, y: int(x) == y)
        self.assertTrue(result.value == '5')

    def test_graph1(self):
        node = DepthLimitedSearchTest.prepare_graph1()
        result = dls(node, '1', 2)
        self.assertTrue(result.value == '1')

    def test_graph2(self):
        node = DepthLimitedSearchTest.prepare_graph1()
        result = dls(node, '10', 10)
        self.assertTrue(result is None)

    def test_graph3(self):
        node = DepthLimitedSearchTest.prepare_graph1()
        result = dls(node, '5', 1)
        self.assertTrue(result is None)

    def test_graph5(self):
        node = DepthLimitedSearchTest.prepare_graph1()
        result = dls(node, '5', 10)
        self.assertTrue(result.value == '5')

    def test_graph4(self):
        node = DepthLimitedSearchTest.prepare_graph1()
        result = dls(node, '6', 4)
        self.assertTrue(result.value == '6')

    def test_graph6(self):
        node = DepthLimitedSearchTest.prepare_graph1()
        result = dls(node, '6', 2)
        self.assertTrue(result is None)