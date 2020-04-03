import unittest  # import the unittest module to test the class methods

from implementation_8.binary_tree import BinaryTree, Node


class TestBinaryTree(unittest.TestCase):
    def test_search(self):
        tree = BinaryTree()
        tree.root = Node(10)
        tree.root.left = Node(20)
        tree.root.left.left = Node(13)
        val = 10
        self.assertEqual(tree.search(val), True)

    def test_search_2(self):
        tree = BinaryTree()
        tree.root = Node(10)
        tree.root.left = Node(20)
        tree.root.left.left = Node(13)
        val = 100
        self.assertEqual(tree.search(val), False)

    def test_preOrderTraversal(self):
        tree = BinaryTree()
        tree.root = Node(10)
        tree.root.left = Node(20)
        tree.root.left.left = Node(13)
        tree.root.left.right = Node(15)
        tree.root.right = Node(60)
        tree.root.right.left = Node(70)
        self.assertEqual(tree.preOrderTraverse(), "10-20-13-15-60-70")

    def test_postOrderTraversal(self):
        tree = BinaryTree()
        tree.root = Node(10)
        tree.root.left = Node(20)
        tree.root.left.left = Node(13)
        tree.root.left.right = Node(15)
        tree.root.right = Node(60)
        tree.root.right.left = Node(70)
        self.assertEqual(tree.postOrderTraversal(), "13-15-20-70-60-10")

    def test_inOrderTraversal(self):
        tree = BinaryTree()
        tree.root = Node(10)
        tree.root.left = Node(20)
        tree.root.left.left = Node(13)
        tree.root.left.right = Node(15)
        tree.root.right = Node(60)
        tree.root.right.left = Node(70)
        self.assertEqual(tree.inOrderTraversal(), "13-20-15-10-70-60")

    def test_height(self):
        tree = BinaryTree()
        tree.root = Node(10)
        tree.root.left = Node(20)
        tree.root.left.left = Node(13)
        tree.root.left.right = Node(15)
        tree.root.right = Node(60)
        tree.root.right.left = Node(70)
        self.assertEqual(tree.height(tree.root), 3)



if __name__ == '__main__':
    unittest.main()
