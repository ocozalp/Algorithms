from unittest.case import TestCase
from data_structures.binary_tree import BinaryTree

class BinaryTreeTest(TestCase):
    def prepare_tree1(self):
        b = BinaryTree()
        b.insert(8)
        b.insert(10)
        b.insert(3)
        b.insert(1)
        b.insert(6)
        b.insert(4)
        b.insert(7)
        b.insert(14)
        b.insert(13)
        return b

    def test_tree1(self):
        b = self.prepare_tree1()

        self.assertTrue(b.contains(13))

    def test_in_order(self):
        b = self.prepare_tree1()
        r = b.in_order()
        print r
        self.assertTrue(r == [1, 3, 4, 6, 7, 8, 10, 13, 14])

    def test_pre_order(self):
        b = self.prepare_tree1()
        r = b.pre_order()
        print r
        self.assertTrue(r == [8, 3, 1, 6, 4, 7, 10, 14, 13])

    def test_post_order(self):
        b = self.prepare_tree1()
        r = b.post_order()
        print r
        self.assertTrue(r == [1, 4, 7, 6, 3, 13, 14, 10, 8])

    def test_delete_leaf(self):
        b = self.prepare_tree1()
        b.delete(13)
        r = b.pre_order()
        print r
        self.assertTrue(r == [8, 3, 1, 6, 4, 7, 10, 14])

    def test_delete_one_child(self):
        b = self.prepare_tree1()
        b.delete(14)
        r = b.pre_order()
        print r
        self.assertTrue(r == [8, 3, 1, 6, 4, 7, 10, 13])

    def test_delete_one_child_2(self):
        b = self.prepare_tree1()
        b.delete(10)
        r = b.pre_order()
        print r
        self.assertTrue(r == [8, 3, 1, 6, 4, 7, 14, 13])

    def test_delete_two_children(self):
        b = self.prepare_tree1()
        b.delete(3)
        r = b.pre_order()
        print r
        self.assertTrue(r == [8, 1, 6, 4, 7, 10, 14, 13])

    def test_delete_two_children_2(self):
        b = self.prepare_tree1()
        b.delete(6)
        r = b.pre_order()
        print r
        self.assertTrue(r == [8, 3, 1, 4, 7, 10, 14, 13])

    def test_delete_root(self):
        b = self.prepare_tree1()
        b.delete(8)
        r = b.pre_order()
        print r
        self.assertTrue(r == [7, 3, 1, 6, 4, 10, 14, 13])