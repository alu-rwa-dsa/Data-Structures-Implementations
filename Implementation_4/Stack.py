class Stack(object):
    """
    class Stack provides implementation of all primary method of a stack such as push, pop, isEmpty, size, and show
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        add a given element to the end of the stack
        """
        self.items.append(item)

    def pop(self):
        """
        delete the last element of the stack
        """
        try:
            self.items.pop()
        except IndexError:
            raise Exception("Stack is empty")

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def size(self):
        return len(self.items)

    def show(self):
        return self.items


