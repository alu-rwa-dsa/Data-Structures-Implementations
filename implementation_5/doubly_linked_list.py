class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.previous = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_head(self):
        if self.head is None:
            return None
        return self.head.data

    def get_tail(self):
        if self.tail is None:
            return None
        return self.tail.data

    def get_size(self):
        return self.size

    def prepend(self, val):
        newNode = Node(val)
        newNode.next = self.head
        newNode.previous = None
        if self.tail is None:
            self.tail = newNode
        if self.head:
            self.head.previous = newNode
        self.head = newNode
        self.size += 1

    def pop_first(self):
        if self.head is None:
            raise IndexError
        else:
            del_val = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return del_val

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            old_tail = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.previous = old_tail
        self.size += 1

    def pop_last(self):
        if self.head is None:
            return None
        last_node = self.tail.data
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        self.size -= 1
        if self.size == 0:
            self.head = None
        return last_node

    def insert_node(self, new_node, previous_node):
        next_node = previous_node.next
        new_node.next = next_node
        new_node.previous = previous_node
        if next_node:
            next_node.previous = new_node
        else:
            self.tail = new_node
        previous_node.next = new_node

        # return a list of all values of the nodes
        n = self.head
        out = []
        for _ in range(self.size):
            n = n.next
            out.append(n.data)
        return out

    def detete_node(self, node):
        prev_node = node.previous
        next_node = node.next
        if (not prev_node) and (not next_node):
            self.head = None
            self.tail = None
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.previous = prev_node
        else:
            self.tail = prev_node



# print(newObj.get_head())
# print(newObj.get_tail())
# print(newObj.pop())
# print(newObj.get_head())
# print(newObj.get_tail())
# print(newObj.pop())
# print(newObj.get_head())
# print(newObj.get_tail())
# print(newObj.pop())
# print(newObj.get_head())
# print(newObj.get_tail())
newObj = DLinkedList()
newObj.append(12)
print(newObj.insert_node(Node(10000), newObj.head))
print(newObj.get_head())
print(newObj.get_tail())
newObj.detete_node(newObj.head.next)
print(newObj.get_head())
print(newObj.get_tail())

