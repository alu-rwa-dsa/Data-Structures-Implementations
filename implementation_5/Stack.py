from single_linked_list import SLinkedList


class Stack(object):
    """
    class Stack provides implementation of all primary method of a stack such as push, pop, isEmpty, size, and show
    """

    def __init__(self):
        self.stack = SLinkedList()

    def show(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        out = []
        current = self.stack.head
        for _ in range(self.stack.size):
            out.append(current.data)
            current = current.next
        return out

    def push(self, val):
        """
        add a given element to the end of the stack
        """
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.stack.append(val)

    def pop(self):
        """
        delete the last element of the stack
        """
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.stack.size > 0:
            return self.stack.pop_last()
        else:
            raise IndexError

    def peek(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.stack.tail.data

    def size(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.stack.size


a = Stack()
a.push(5)
print(a.show())
a.push(6)
a.push(6)
a.push(6)
print(a.show())
a.pop()
print(a.peek())
print(a.show())

