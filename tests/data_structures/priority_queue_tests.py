from unittest.case import TestCase
from data_structures.priority_queue import PriorityQueue


class Deneme:
    def __init__(self, label, val):
        self.label = label
        self.val = val

    def __ge__(self, other):
        return self.val >= other.val

    def __gt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return self.label + ' ' + str(self.val)


class PQTests(TestCase):
    def test_insert(self):
        pq = PriorityQueue()
        pq.add_element(1)

        self.assertTrue(pq.elements[0] == 1)
        for i in xrange(1, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

    def test_insert2(self):
        pq = PriorityQueue()
        pq.add_element(6)
        pq.add_element(5)
        pq.add_element(4)

        self.assertTrue(pq.elements[0] == 6)
        self.assertTrue(pq.elements[1] == 5)
        self.assertTrue(pq.elements[2] == 4)
        for i in xrange(3, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

    def test_insert3(self):
        pq = PriorityQueue()
        pq.add_element(5)
        pq.add_element(4)
        pq.add_element(6)

        self.assertTrue(pq.elements[0] == 6)
        self.assertTrue(pq.elements[1] == 4)
        self.assertTrue(pq.elements[2] == 5)
        for i in xrange(3, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

    def test_insert4(self):
        pq = PriorityQueue()
        pq.add_element(5)
        pq.add_element(4)
        pq.add_element(6)
        pq.add_element(6)
        pq.add_element(3)
        pq.add_element(7)

        self.assertTrue(pq.elements[0] == 7)
        self.assertTrue(pq.elements[1] == 6)
        self.assertTrue(pq.elements[2] == 6)
        self.assertTrue(pq.elements[3] == 4)
        self.assertTrue(pq.elements[4] == 3)
        self.assertTrue(pq.elements[5] == 5)

        for i in xrange(6, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

    def test_delete(self):
        pq = PriorityQueue()
        pq.add_element(5)
        pq.add_element(4)
        pq.add_element(6)
        pq.add_element(6)
        pq.add_element(3)
        pq.add_element(7)

        self.assertTrue(pq.elements[0] == 7)
        self.assertTrue(pq.elements[1] == 6)
        self.assertTrue(pq.elements[2] == 6)
        self.assertTrue(pq.elements[3] == 4)
        self.assertTrue(pq.elements[4] == 3)
        self.assertTrue(pq.elements[5] == 5)

        for i in xrange(6, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

        res = pq.pop()
        self.assertTrue(res == 7)

    def test_batch_increment(self):
        pq = PriorityQueue()
        pq.add_element(Deneme('a', 1))
        pq.add_element(Deneme('b', 5))
        pq.add_element(Deneme('b', 10))
        pq.add_element(Deneme('a', 7))
        pq.add_element(Deneme('a', 9))
        pq.add_element(Deneme('b', 12))

        self.assertTrue(pq.elements[0].val == 12)
        self.assertTrue(pq.elements[1].val == 9)
        self.assertTrue(pq.elements[2].val == 10)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 7)
        self.assertTrue(pq.elements[5].val == 5)

        for i in xrange(6, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

        def validate(obj):
            return obj.label == 'a'

        def update(obj):
            obj.val += 1

        pq.batch_increment(validate, update)
        self.assertTrue(pq.elements[0].val == 12)
        self.assertTrue(pq.elements[1].val == 10)
        self.assertTrue(pq.elements[2].val == 10)
        self.assertTrue(pq.elements[3].val == 2)
        self.assertTrue(pq.elements[4].val == 8)
        self.assertTrue(pq.elements[5].val == 5)

    def test_batch_increment2(self):
        pq = PriorityQueue()
        pq.add_element(Deneme('a', 1))
        pq.add_element(Deneme('c', 5))
        pq.add_element(Deneme('b', 10))
        pq.add_element(Deneme('c', 7))
        pq.add_element(Deneme('a', 9))
        pq.add_element(Deneme('b', 12))

        self.assertTrue(pq.elements[0].val == 12)
        self.assertTrue(pq.elements[1].val == 9)
        self.assertTrue(pq.elements[2].val == 10)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 7)
        self.assertTrue(pq.elements[5].val == 5)

        for i in xrange(6, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

        def validate(obj):
            return obj.label == 'c'

        def update(obj):
            obj.val += 6

        pq.batch_increment(validate, update)
        self.assertTrue(pq.elements[0].val == 13)
        self.assertTrue(pq.elements[1].val == 12)
        self.assertTrue(pq.elements[2].val == 11)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 9)
        self.assertTrue(pq.elements[5].val == 10)

    def test_batch_decrement(self):
        pq = PriorityQueue()
        pq.add_element(Deneme('a', 1))
        pq.add_element(Deneme('b', 5))
        pq.add_element(Deneme('b', 10))
        pq.add_element(Deneme('a', 7))
        pq.add_element(Deneme('a', 9))
        pq.add_element(Deneme('c', 12))

        self.assertTrue(pq.elements[0].val == 12)
        self.assertTrue(pq.elements[1].val == 9)
        self.assertTrue(pq.elements[2].val == 10)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 7)
        self.assertTrue(pq.elements[5].val == 5)

        for i in xrange(6, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

        def validate(obj):
            return obj.label == 'c'

        def update(obj):
            obj.val -= 13

        pq.batch_decrement(validate, update)
        self.assertTrue(pq.elements[0].val == 10)
        self.assertTrue(pq.elements[1].val == 9)
        self.assertTrue(pq.elements[2].val == 5)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 7)
        self.assertTrue(pq.elements[5].val == -1)

    def test_batch_decrement2(self):
        pq = PriorityQueue()
        pq.add_element(Deneme('a', 1))
        pq.add_element(Deneme('b', 5))
        pq.add_element(Deneme('c', 10))
        pq.add_element(Deneme('a', 7))
        pq.add_element(Deneme('c', 9))
        pq.add_element(Deneme('a', 12))

        self.assertTrue(pq.elements[0].val == 12)
        self.assertTrue(pq.elements[1].val == 9)
        self.assertTrue(pq.elements[2].val == 10)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 7)
        self.assertTrue(pq.elements[5].val == 5)

        for i in xrange(6, len(pq.elements)):
            self.assertTrue(pq.elements[i] is None)

        def validate(obj):
            return obj.label == 'c'

        def update(obj):
            obj.val -= 6

        pq.batch_decrement(validate, update)
        self.assertTrue(pq.elements[0].val == 12)
        self.assertTrue(pq.elements[1].val == 7)
        self.assertTrue(pq.elements[2].val == 5)
        self.assertTrue(pq.elements[3].val == 1)
        self.assertTrue(pq.elements[4].val == 3)
        self.assertTrue(pq.elements[5].val == 4)