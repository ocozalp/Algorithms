class BinaryTree:

    class BinaryTreeNode:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryTree.BinaryTreeNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, local_root, value):
        if local_root.value != value:
            if local_root.value > value:
                if local_root.left is None:
                    local_root.left = BinaryTree.BinaryTreeNode(value)
                else:
                    self.__insert(local_root.left, value)
            else:
                if local_root.right is None:
                    local_root.right = BinaryTree.BinaryTreeNode(value)
                else:
                    self.__insert(local_root.right, value)

    def contains(self, value):
        return self.__contains(self.root, value)

    def __contains(self, local_root, value):
        if local_root is None:
            return False

        if local_root.value == value:
            return True

        if local_root.value > value:
            return self.__contains(local_root.left, value)

        return self.__contains(local_root.right, value)

    def pre_order(self):
        result = list()
        self.__pre_order(self.root, result)
        return result

    def __pre_order(self, local_root, result):
        if local_root is not None:
            result.append(local_root.value)
            self.__pre_order(local_root.left, result)
            self.__pre_order(local_root.right, result)

    def in_order(self):
        result = list()
        self.__in_order(self.root, result)
        return result

    def __in_order(self, local_root, result):
        if local_root is not None:
            self.__in_order(local_root.left, result)
            result.append(local_root.value)
            self.__in_order(local_root.right, result)

    def post_order(self):
        result = list()
        self.__post_order(self.root, result)
        return result

    def __post_order(self, local_root, result):
        if local_root is not None:
            self.__post_order(local_root.left, result)
            self.__post_order(local_root.right, result)
            result.append(local_root.value)

    def delete(self, value):
        self.__delete(None, self.root, value)

    def __delete(self, parent_node, local_root, value):
        if local_root is None:
            return None

        if local_root.value < value:
            return self.__delete(local_root, local_root.right, value)
        elif local_root.value > value:
            return self.__delete(local_root, local_root.left, value)
        else:
            if local_root.right is not None and local_root.left is not None:
                max_left_child = self.__find_max(local_root.left)
                new_value = max_left_child.value
                self.delete(new_value)
                local_root.value = new_value
            elif local_root.right is not None:
                self.__set_child_of_parent(parent_node, local_root.right, value)
            elif local_root.left is not None:
                self.__set_child_of_parent(parent_node, local_root.left, value)
            else:
                self.__set_child_of_parent(parent_node, None, value)

    def __find_max(self, local_root):
        while local_root.right is not None:
            local_root = local_root.right
        return local_root

    def __set_child_of_parent(self, parent, child, value):
        if parent is None:
            self.root = child
        elif parent.value > value:
            parent.left = child
        else:
            parent.right = child