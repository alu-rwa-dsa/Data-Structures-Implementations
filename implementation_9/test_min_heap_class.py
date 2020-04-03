import unittest  # import the unittest module to test the class methods

from implementation_9.min_heap_class import MinHeap


class TestMinHeapClass(unittest.TestCase):
    def testGetMin(self):
        arr = [5, 2, 11, 0, 3, 1, 7]
        heap = MinHeap(arr)
        self.assertEqual(heap.getMinimum(), 0)

    def testExtractMin(self):
        arr = [5, 2, 11, 0, 3, 1, 7]
        heap = MinHeap(arr)
        self.assertEqual(heap.getMinimum(), 0)

    def testInsert(self):
        arr = [5, 2, 11, 0, 3, 1, 7]
        heap = MinHeap(arr)
        self.assertEqual(heap.insert(-1), [-1, 0, 1, 2, 3, 11, 7, 5])

    def testInsert_2(self):
        arr = [5, 2, 11, 0, 3, 1, 7]
        heap = MinHeap(arr)
        self.assertEqual(heap.insert(1), [0, 1, 1, 2, 3, 11, 7, 5])

    def testDelete(self):
        arr = [5, 2, 11, 0, 3, 1, 7]
        heap = MinHeap(arr)
        self.assertEqual(heap.delete(1), 2)


if __name__ == '__main__':
    unittest.main()