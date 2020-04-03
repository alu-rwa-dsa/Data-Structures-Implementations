import unittest  # import the unittest module to test the class methods

from implementation_9.create_min_heap import createMinHeap


class TestMinHeap(unittest.TestCase):
    def test1(self):
        arr = [1]
        self.assertEqual(createMinHeap(arr), [1])

    def test2(self):
        arr = [5, 2, 11, 0, 3, 1, 7]
        self.assertEqual(createMinHeap(arr), [0, 2, 1, 5, 3, 11, 7])

    def test3(self):
        arr = [5, 2, 11, 0, 3, 7]
        self.assertEqual(createMinHeap(arr), [0, 2, 7, 5, 3, 11])

    def test4(self):
        arr = []
        self.assertEqual(createMinHeap(arr), [])


if __name__ == '__main__':
    unittest.main()