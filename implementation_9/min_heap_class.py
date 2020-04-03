from implementation_9.create_min_heap import createMinHeap, minHeapify


class MinHeap(object):
    def __init__(self, arr):
        self.min_heap = createMinHeap(arr)

    def show_heap(self):
        return self.min_heap

    def getMinimum(self):
        """
        getMinimum return the integer of the min value in the min heap
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        return self.min_heap[0]

    def extractMinimum(self):
        """
        extractMinimum deletes the first element of the min heap and returns its value
        TimeComplexity: O(h) where h is the height of the tree
        SpaceComplexity: O(1)
        """
        self.min_heap[0] = self.min_heap[-1]
        min_val = self.min_heap.pop()
        minHeapify(self.min_heap, len(self.min_heap), 0)
        return min_val








