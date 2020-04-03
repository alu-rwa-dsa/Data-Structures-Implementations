import unittest  # import the unittest module to test the class methods

from implementation_9.heap_sort import heapSort


class TestSLinkedList(unittest.TestCase):
    def test1(self):
        l = [5, 3, 12, 2, 1]
        self.assertEqual(heapSort(l), [1, 2, 3, 5, 12])

    def test2(self):
        l = []
        self.assertEqual(heapSort(l), [])

    def test3(self):
        l = [4, 4, 1, 1, 0]
        self.assertEqual(heapSort(l), [0, 1, 1, 4, 4])


if __name__ == '__main__':
    unittest.main()
