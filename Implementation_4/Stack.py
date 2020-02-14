class Stack(object):
    """
    class Stack provides implementation of all primary method of a stack such as push, pop, isEmpty, size, and show
    """

    def __init__(self):
        self.stack = []

    def show(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.stack

    def push(self, item):
        """
        add a given element to the end of the stack
        """
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.stack.append(item)

    def pop(self):
        """
        delete the last element of the stack
        """
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.size() > 0:
            self.stack.pop()
        else:
            raise IndexError

    def peek(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        try:
            return self.stack[-1]
        except IndexError:
            return None

    def size(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return len(self.stack)


