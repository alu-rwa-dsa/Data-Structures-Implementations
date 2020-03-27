"""
Create BinaryTreeNode and BinaryTree Classes including the primary methods.
Methods:
    1- Insert
    2- Delete
    3- Search for the existence of a specific value
    4- Traverse:
        Pre-order traversal
        In-order traversal
        Post-order traversal
# Write an algorithm to compute the height of the binary tree.
"""


class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.number_of_elements = 1

    def search(self, val):
        start = self.root
        return self.preOrderTraverseSearch(start, val)

    def preOrderTraverseSearch(self, start, val):
        if start:
            if start.value == val:
                return True
            else:
                return self.preOrderTraverseSearch(start.left, val) or self.preOrderTraverseSearch(start.right, val)
        return False

    def preOrderTraverse(self):
        traverse = ""
        return self.__preOrderTraverse(self.root, traverse)[:-1]

    def __preOrderTraverse(self, root, traverse):
        if root:
            traverse += str(root.value) + "-"
            traverse = self.__preOrderTraverse(root.left, traverse)
            traverse = self.__preOrderTraverse(root.right, traverse)
        return traverse

    def inOrderTraversal(self):
        traverse = ""
        return self.__inOrderTraversal(self.root, traverse)[:-1]

    def __inOrderTraversal(self, root, traverse):
        if root:
            traverse = self.__inOrderTraversal(root.left, traverse)
            traverse += str(root.value) + "-"
            traverse = self.__inOrderTraversal(root.right, traverse)
        return traverse

    def postOrderTraversal(self):
        traverse = ""
        return self.__postOrderTraversal(self.root, traverse)[:-1]

    def __postOrderTraversal(self, root, traverse):
        if root:
            traverse = self.__postOrderTraversal(root.left, traverse)
            traverse = self.__postOrderTraversal(root.right, traverse)
            traverse += str(root.value) + "-"
        return traverse
