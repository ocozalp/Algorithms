__author__ = 'orhan'

from unionfind.quickunion import QuickUnion


class WeightedQuickUnion(QuickUnion):

    def __init__(self, n):
        QuickUnion.__init__(self, n)
        self.item_counts = [1] * n

    def connect(self, item1, item2):
        pid1 = self.parent(item1)
        pid2 = self.parent(item2)
        if self.item_counts[pid1] > self.item_counts[pid2]:
            self.arr[pid2] = pid1
            self.item_counts[pid1] += self.item_counts[pid2]
        else:
            self.arr[pid1] = pid2
            self.item_counts[pid2] += self.item_counts[pid1]