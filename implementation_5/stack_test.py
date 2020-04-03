"""
Test all function in the stack class
"""
import unittest  # import the unittest module to test the class methods

from implementation_5.Stack import Stack


class TestStacks(unittest.TestCase):
    def test_push(self):
        """
        test pushing multi element to the stack
        """
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        self.assertEqual(stack1.show(), [5, 6])

    def test_peek(self):
        """
        test peek of a stack
        """
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        self.assertEqual(stack1.peek(), 6)

    def test_empty_peek(self):
        """
        test peek of an empty stack
        """
        stack1 = Stack()  # stack1 is an instance of stack class
        self.assertEqual(stack1.peek(), None)

    def test_size(self):
        """
        test size of a stack
        """
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        self.assertEqual(stack1.size(), 2)

    def test_pop(self):
        """
        test delete elements from a non empty stack
        """
        stack1 = Stack()  # stack1 is an instance of stack class
        stack1.push(5)
        stack1.push(6)
        stack1.pop()
        self.assertEqual(stack1.show(), [5])

    def test_empty_pop(self):
        """
        test delete elements from an empty stack
        """
        stack1 = Stack()
        with self.assertRaises(IndexError):
            stack1.pop()


if __name__ == '__main__':
    unittest.main()
