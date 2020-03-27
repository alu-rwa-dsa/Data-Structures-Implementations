import unittest  # import the unittest module to test the class methods

from binary_search_tree import BST


class TestBSTTree(unittest.TestCase):
    def test_BST_insert(self):
        # Set up tree
        tree = BST()
        self.assertEqual(tree.createBST([1, 2, 0, 4, 1.5]), "0-1-1.5-2-4")

    def test_search(self):
        tree = BST()
        tree.createBST([1, 2, 0, 4, 1.5])
        val = 3
        self.assertEqual(tree.search(val), False)

    def test_search_2(self):
        tree = BST()
        tree.createBST([1, 2, 0, 4, 1.5])
        val = 2
        self.assertEqual(tree.search(val), True)


if __name__ == '__main__':
    unittest.main()
