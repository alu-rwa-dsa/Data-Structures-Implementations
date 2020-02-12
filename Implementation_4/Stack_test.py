"""
Test all function in the stack class
"""

from Stack import Stack


import unittest  # import the unittest module to test the class methods


class TestTaskThree(unittest.TestCase):
    def test_push(self):
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        self.assertEqual(stack1.show(), [5, 6])

    def test_peek(self):
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        self.assertEqual(stack1.peek(), 6)

    def test_size(self):
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        self.assertEqual(stack1.size(), 2)

    def test_pop(self):
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        stack1.pop()
        self.assertEqual(stack1.show(), [5])


if __name__ == '__main__':
    unittest.main()