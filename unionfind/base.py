__author__ = 'orhan'


class UnionFind(object):

    def __init__(self, n):
        self.n = n
        self.__initArray()

    def __initArray(self):
        self.arr = [i for i in xrange(self.n)]

    def connect(self, item1, item2):
        raise Exception("Not implemented")

    def parent(self, index):
        raise Exception("Not implemented")

    def isConnected(self, item1, item2):
        return self.parent(item1) == self.parent(item2)