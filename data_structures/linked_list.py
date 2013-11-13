from common.data_structures import LinkedNode


class LinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def add(self, value):
        if self.__head is None:
            self.__head = LinkedNode(value)
            self.__tail = self.__head
        else:
            new_node = LinkedNode(value)
            self.__tail.set_next(new_node)
            self.__tail = new_node

        self.__count += 1

    def remove(self, value):
        parent = None
        node = self.__head

        while node is not None and node.value != value:
            parent = node
            node = node.get_next()

        if node is not None:
            if parent is None:
                self.__head = node.get_next()
            else:
                parent.set_next(node.get_next())

            if node.get_next() is None:
                self.__tail = parent

            self.__count -= 1

    def __len__(self):
        return self.__count

    def get_item_at(self, i):
        if i >= self.__count or i < 0:
            return None

        index = 0
        node = self.__head
        while index < i:
            node = node.get_next()
            index += 1

        return node.value

    def remove_item_at(self, i):
        if i >= self.__count or i < 0:
            return None

        index = 0
        node = self.__head
        parent = None
        while index < i:
            parent = node
            node = node.get_next()
            index += 1

        if parent is None:
            self.__head = self.__head.get_next()
        else:
            parent.set_next(node.get_next())

        if node.get_next() is None:
            self.__tail = parent

        self.__count -= 1
        return node.value