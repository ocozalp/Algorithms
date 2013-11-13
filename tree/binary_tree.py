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
            if local_root.value < value:
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

        if local_root.value < value:
            return self.__contains(local_root.left, value)

        return self.__contains(local_root.right, value)

    def pre_order(self):
        return self.__pre_order(self.root)

    def __pre_order(self, local_root):
        if local_root is not None:
            print local_root.value
            self.__pre_order(local_root.left)
            self.__pre_order(local_root.right)

    def in_order(self):
        return self.__in_order(self.root)

    def __in_order(self, local_root):
        if local_root is not None:
            self.__in_order(local_root.left)
            print local_root.value
            self.__in_order(local_root.right)

    def post_order(self):
        return self.__post_order(self.root)

    def __post_order(self, local_root):
        if local_root is not None:
            self.__post_order(local_root.left)
            self.__post_order(local_root.right)
            print local_root.value