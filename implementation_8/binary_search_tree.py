class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.len = 0
        self.root = None

    def createBST(self, l):
        """
        Time Complexity: O(n*log(n))
        Space_Complexity: O(1)
        """
        # update the length of the BST
        self.len = len(l)
        # check if the list is empty
        if len(l) < 1:
            return ""
        for ele in l:
            # check if there is a root
            if not self.root:
                self.root = Node(ele)
            # if the root exists, insert every element
            else:
                self.__insert_ele(self.root, ele)
        return self.inOrderTraversal()

    # private helper method to insert the elements in their right position
    def __insert_ele(self, start, val):
        if start.value < val:
            if start.right:
                self.__insert_ele(start.right, val)
            else:
                start.right = Node(val)
        elif start.value > val:
            if start.left:
                self.__insert_ele(start.left, val)
            else:
                start.left = Node(val)

    def search(self, val):
        """
        Time Complexity: O(log(n))
        Space_Complexity: O(1)
        """
        start = self.root
        while start:
            if start.value == val:
                return True
            elif start.value > val:
                start = start.left
            else:
                start = start.right
        return False

    def searchRecursive(self, val):
        """
        Time Complexity: O(log(n))
        Space_Complexity: O(1)
        """

        def __helper(val, root):
            if root:
                if root.value == val:
                    return True
                elif root.value > val:
                    return __helper(val, root.left)
                else:
                    return __helper(val, root.right)
            else:
                return False

        return __helper(val, self.root)

    # inOrderTraversal returns the values of nodes in the tree as sorted list (ASC order)
    def inOrderTraversal(self):
        """
        Time Complexity: O(n)
        Space_Complexity: O(1)
        """
        traverse = []
        f = self.__inOrderTraversal(self.root)
        for _ in range(self.len):
            traverse.append(next(f))
        return traverse

    def __inOrderTraversal(self, root):
        if root:
            yield from self.__inOrderTraversal(root.left)
            yield root.value
            yield from self.__inOrderTraversal(root.right)


    # find the kth smallest element in the BST
    def kthSmallestInBST(self, root, K):
        f = self.__inOrderTraversal(root)
        for _ in range(K):
            ans = next(f)
        return ans

    # check if a binary search tree is valid or not
    def isValid(self, root):
        f = self.__inOrderTraversal(root)
        if root:
            pre = next(f)
            while True:
                try:
                    new = next(f)
                    if new <= pre:
                        return False
                    pre = new
                except:
                    return True
        else:
            return True



t = BST()
t.createBST([0])
print(t.isValid(t.root))