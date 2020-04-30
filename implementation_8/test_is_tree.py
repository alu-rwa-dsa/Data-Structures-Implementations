import unittest  # import the unittest module to test the class methods

from implementation_8.is_tree import isTree


class TestIsTree(unittest.TestCase):
    def test_tree(self):
        tree = [3, [4, [5], [6]], [2, [1], [2]]]
        self.assertEqual(isTree(tree), True)

    def test_tree_2(self):
        tree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
        self.assertEqual(isTree(tree), True)

    def test_false_tree(self):
        # tree without a root
        tree = [[4, [5], [6]], [2, [1], [2]]]
        self.assertEqual(isTree(tree), False)

    def test_empty_tree(self):
        # tree without a root
        tree = []
        self.assertEqual(isTree(tree), True)


if __name__ == '__main__':
    unittest.main()
