"""
Create BinaryTreeNode and BinaryTree Classes including the primary methods.
Methods:
    1- Search for the existence of a specific value
    2- Traverse:
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

    def search(self, val):
        """
        Time_Complexity: O(n)
        Space_complexity: O(1)
        """
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
        """
        Time_Complexity: O(n)
        Space_complexity: O(1)
        """
        traverse = ""
        return self.__preOrderTraverse(self.root, traverse)[:-1]

    def __preOrderTraverse(self, root, traverse):
        if root:
            traverse += str(root.value) + "-"
            traverse = self.__preOrderTraverse(root.left, traverse)
            traverse = self.__preOrderTraverse(root.right, traverse)
        return traverse

    def inOrderTraversal(self):
        """
        Time_Complexity: O(n)
        Space_complexity: O(1)
        """
        traverse = ""
        return self.__inOrderTraversal(self.root, traverse)[:-1]

    def __inOrderTraversal(self, root, traverse):
        if root:
            traverse = self.__inOrderTraversal(root.left, traverse)
            traverse += str(root.value) + "-"
            traverse = self.__inOrderTraversal(root.right, traverse)
        return traverse

    def postOrderTraversal(self):
        """
        Time_Complexity: O(n)
        Space_complexity: O(1)
        """
        traverse = ""
        return self.__postOrderTraversal(self.root, traverse)[:-1]

    def __postOrderTraversal(self, root, traverse):
        if root:
            traverse = self.__postOrderTraversal(root.left, traverse)
            traverse = self.__postOrderTraversal(root.right, traverse)
            traverse += str(root.value) + "-"
        return traverse

    def height(self, node):
        """
        Time_Complexity: O(n)
        Space_complexity: O(1)
        """
        if node is None:
            return -1
        else:
            leftHeight = self.height(node.left) + 1
            rightHeight = self.height(node.right) + 1
            return max(leftHeight, rightHeight)

    def hasPathSum(self, root, sum):
        """
        check if the sum of all nodes in a branch from root to leaf == sum
        """
        l_sum = 0
        r_sum = 0
        if root:
            l_sum += root.value + self.hasPathSum(root.left, sum)
            r_sum += root.value + self.hasPathSum(root.right, sum)
        else:
            return l_sum == sum or r_sum == sum

t = BinaryTree()
t.root = Node(5)
t.root.left = Node(4)
t.root.right = Node(8)
t.root.left.left = Node(11)
t.root.left.left.left = Node(7)
t.root.left.left.right = Node(2)
t.root.left.left.right = Node(2)
t.root.right.left = Node(13)
t.root.right.right = Node(4)
print(t.hasPathSum(t.root, 22))
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
#
