class Queue:
    """
    Queue Stack provides implementation of all primary method of a queue such as enqueue, dequeue, peek
    """

    def __init__(self):
        self.queue = []

    def show(self):
        return self.queue

    def enqueue(self, val):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.queue.append(val)

    def dequeue(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        self.queue.pop(0)

    def peek(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.queue[0]

