class Node(object):

    def __init__(self):
        self.children = list()

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, index):
        return self.children[index]

    def __iter__(self):
        return iter(self.children)

    def __eq__(self, other):
        return self.value == other.value


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next