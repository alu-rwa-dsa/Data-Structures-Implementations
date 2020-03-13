import unittest  # import the unittest module to test the class methods

from special_sort import specialSort


class TestSLinkedList(unittest.TestCase):
    def test1(self):
        alist = [[2, 2], [1, 10], [5, 4], [1, 4]]
        self.assertEqual(specialSort(alist), [[2, 2], [1, 4], [5, 4], [1, 10]])

    def test2(self):
        alist = []
        self.assertEqual(specialSort(alist), [])

    def test3(self):
        alist = [[4, 0], [1, 0]]
        self.assertEqual(specialSort(alist), [[1, 0], [4, 0]])


if __name__ == '__main__':
    unittest.main()
