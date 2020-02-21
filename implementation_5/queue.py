from single_linked_list import SLinkedList


class Queue:
    """
    Queue Stack provides implementation of all primary method of a queue such as enqueue, dequeue, peek
    """

    def __init__(self):
        self.queue = SLinkedList

    def show(self):
        out = []
        current = self.queue.head
        for _ in range(self.queue.size):
            out.append(current.data)
            current = current.next
        return out

    def enqueue(self, val):
        """
        add a given element to the end of the queue
        """
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.queue.append(val)

    def dequeue(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.queue.size > 0:
            return self.queue.pop_first()
        else:
            raise IndexError

    def peek(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.queue.head.data


a = Queue()
a.enqueue(1200)
print(a.show())
a.enqueue(120)
a.dequeue()
print(a.peek())
