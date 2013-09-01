__author__ = 'orhan'

from unionfind.base import UnionFind


class QuickFind(UnionFind):

    def __init__(self, n):
        UnionFind.__init__(self, n)

    def parent(self, index):
        return self.arr[index]

    def connect(self, item1, item2):
        pid1 = self.arr[item1]
        pid2 = self.arr[item2]

        for i in xrange(self.n):
            if self.arr[i] == pid2:
                self.arr[i] = pid1