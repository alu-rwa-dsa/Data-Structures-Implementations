"""
Test all function in the stack class
"""

from queue import Queue

import unittest  # import the unittest module to test the class methods


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()  # initialize queue1 as an instance of Queue class
        queue.enqueue(5)
        queue.enqueue(6)
        self.assertEqual(queue.show(), [5, 6])

    def test_peek(self):
        queue = Queue()  # initialize queue1 as an instance of Queue class
        queue.enqueue(5)
        queue.enqueue(6)
        self.assertEqual(queue.peek(), 5)
        self.assertNotEqual(queue.peek(), 6)

    def test_empty_peek(self):
        """
        test peek of an empty queue
        """
        queue = Queue()  # stack1 is an instance of stack class
        self.assertEqual(queue.peek(), None)

    def test_dequeue(self):
        """
        test deleting elements from an non-empty queue
        """
        queue = Queue()  # initialize queue1 as an instance of Queue class
        queue.enqueue(5)
        queue.enqueue(6)
        queue.dequeue()
        self.assertEqual(queue.show(), [6])

    def test_empty_pop(self):
        """
        test deleting elements from an empty queue
        """
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()


if __name__ == '__main__':
    unittest.main()

