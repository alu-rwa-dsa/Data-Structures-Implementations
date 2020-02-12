class Queue:
    """
    Queue Stack provides implementation of all primary method of a queue such as enqueue, dequeue, peek
    """

    def __init__(self):
        self.queue = []

    def show(self):
        return self.queue

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]


a = Queue()
a.enqueue(5)
print(a)
a.enqueue(6)
a.dequeue()
print(a.peek())
