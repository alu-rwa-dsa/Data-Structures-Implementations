"""
Test all function in the stack class
"""

from Implementation_4.queue import Queue


import unittest  # import the unittest module to test the class methods


class TestTaskThree(unittest.TestCase):
    def test_enqueue(self):
        queue1 = Queue()  # initialize queue1 as an instance of Queue class
        queue1.enqueue(5)
        queue1.enqueue(6)
        self.assertEqual(queue1.show(), [5, 6])

    def test_peek(self):
        queue1 = Queue()  # initialize queue1 as an instance of Queue class
        queue1.enqueue(5)
        queue1.enqueue(6)
        self.assertEqual(queue1.peek(), 5)
        self.assertNotEqual(queue1.peek(), 6)

    def test_dequeue(self):
        queue1 = Queue()  # initialize queue1 as an instance of Queue class
        queue1.enqueue(5)
        queue1.enqueue(6)
        queue1.dequeue()
        self.assertEqual(queue1.show(), [6])


if __name__ == '__main__':
    unittest.main()