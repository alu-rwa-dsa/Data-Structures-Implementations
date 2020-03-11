class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def show_tree(self):
        traverse = ""
        return self.preOrderTraverse(self.root, traverse)

    def preOrderTraverse(self, root, traverse):
        if root:
            traverse += str(root.value) + "-"
            traverse = self.preOrderTraverse(root.left, traverse)
            traverse = self.preOrderTraverse(root.right, traverse)
            print(traverse)
        return traverse


newTree = BinaryTree(10)
newTree.root.left = Node(20)
newTree.root.left.left = Node(13)
newTree.root.left.right = Node(15)
newTree.root.right = Node(60)
newTree.root.right.right = Node(70)
print(newTree.show_tree())
