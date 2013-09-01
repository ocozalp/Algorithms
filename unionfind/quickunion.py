__author__ = 'orhan'

from unionfind.base import UnionFind


class QuickUnion(UnionFind):

    def __init__(self, n):
        UnionFind.__init__(self, n)

    def connect(self, item1, item2):
        pid1 = self.parent(item1)
        pid2 = self.parent(item2)
        self.arr[pid2] = pid1

    def parent(self, index):
        current_item = index
        while self.arr[current_item] != current_item:
            current_item = self.arr[current_item]

        return current_item