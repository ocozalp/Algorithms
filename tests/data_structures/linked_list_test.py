from unittest.case import TestCase
from data_structures.linked_list import LinkedList


class LinkedListTests(TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)

    def test_single_item(self):
        ll = LinkedList()
        ll.add(1)

        self.assertEqual(len(ll), 1)

    def test_remove_item(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)

        self.assertEqual(len(ll), 2)
        ll.remove(1)
        self.assertEqual(len(ll), 1)

    def test_index(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)

        self.assertEqual(ll.remove_item_at(0), 1)

    def test_remove_index(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)

        ll.remove_item_at(0)
        self.assertEqual(ll.get_item_at(0), 2)