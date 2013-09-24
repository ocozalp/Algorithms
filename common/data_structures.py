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