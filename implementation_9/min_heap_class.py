from implementation_9.create_min_heap import createMinHeap, minHeapify


class MinHeap(object):
    def __init__(self, arr):
        self.min_heap = createMinHeap(arr)

    def __str__(self):
        return str(self.min_heap)

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
        # swap the first and last element
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        # delete the last element (the min number in the heap)
        min_val = self.min_heap.pop()
        # heapify the subtree of the first element
        minHeapify(self.min_heap, len(self.min_heap), 0)
        return min_val

    def insert(self, val):
        """
        insert takes in a value to be added at the end of the heap with preserving the identity of the min heap
        TimeComplexity: O(h) where h is the height of the tree
        SpaceComplexity: O(1)
        """
        # append the new value at the end of the min_heap
        self.min_heap.append(val)
        # get the index of the inserted value
        val_ind = len(self.min_heap) - 1
        # compare the inserted value to its parent, and swap it with its parent while its value is less than
        # its parent
        while self.min_heap[val_ind] < self.min_heap[(val_ind-1)//2]:
            self.min_heap[val_ind], self.min_heap[(val_ind-1)//2] = self.min_heap[(val_ind-1)//2], self.min_heap[val_ind]
            val_ind = (val_ind-1)//2
        return self.min_heap

    def delete(self, ind):
        """
        Delete(ind) - deletes value at a specific index from the heap preserving the identity of the min heap
            - Delete the last element
            - Heapify the new element in index, ind.
        """
        # Swap the element in the given index, ind, with the last element
        self.min_heap[ind], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        # Delete the last element
        deleted_val = self.min_heap.pop()
        # heapify the element in index = ind
        minHeapify(self.min_heap, len(self.min_heap), ind)
        return deleted_val


if __name__ == "__main__":
    m_heap = MinHeap([50, 40, 30, 20, 12, 10, 1])
    print(m_heap.insert(2))
