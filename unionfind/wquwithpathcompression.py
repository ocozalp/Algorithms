__author__ = 'orhan'

from unionfind.weightedquickunion import WeightedQuickUnion


class WQUWithPathCompression(WeightedQuickUnion):

    def __init__(self, n):
        WeightedQuickUnion.__init__(self, n)

    def parent(self, index):
        current_item = index
        while self.arr[current_item] != current_item:
            current_item = self.arr[current_item]

        update_index = index
        while self.arr[update_index] != current_item:
            parent_index = self.arr[update_index]
            self.arr[update_index] = current_item
            update_index = parent_index

        return current_item