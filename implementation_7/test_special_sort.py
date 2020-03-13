import unittest  # import the unittest module to test the class methods

from binary_search import binarySearch


class TestSLinkedList(unittest.TestCase):
    def test1(self):
        l = [1, 2, 3, 4, 5, 6]
        target = 4
        self.assertEqual(binarySearch(l, target), True)

    def test2(self):
        l = []
        target = 4
        self.assertEqual(binarySearch(l, target), False)

    def test3(self):
        l = [1, 2, 3, 4, 5, 6]
        target = 120
        self.assertEqual(binarySearch(l, target), False)

    def test4(self):
        l = [1, 2, 3, 4, 5, 6]
        target = 1
        self.assertEqual(binarySearch(l, target), True)


if __name__ == '__main__':
    unittest.main()
