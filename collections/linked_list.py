from common.data_structures import LinkedNode

'''
Still incomplete.
I have to go out and smoke waterpipe with my cousin :)
'''
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            self.head = LinkedNode(value)
            self.tail = self.head
        else:
            new_node = LinkedNode(value)
            self.tail.set_next(new_node)
            self.tail = new_node