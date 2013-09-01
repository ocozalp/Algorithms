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
        currentitem = index
        while self.arr[currentitem] != currentitem:
            currentitem = self.arr[currentitem]

        return currentitem