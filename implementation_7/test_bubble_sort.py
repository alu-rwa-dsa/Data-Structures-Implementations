import unittest  # import the unittest module to test the class methods

from bubble_sort import bubbleSort


class TestSLinkedList(unittest.TestCase):
    def test1(self):
        l = [5, 3, 12, 2, 1]
        self.assertEqual(bubbleSort(l), [1, 2, 3, 5, 12])

    def test2(self):
        l = []
        self.assertEqual(bubbleSort(l), [])

    def test3(self):
        l = [4, 4, 1, 1, 0]
        self.assertEqual(bubbleSort(l), [0, 1, 1, 4, 4])


if __name__ == '__main__':
    unittest.main()
