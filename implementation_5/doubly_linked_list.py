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

    def insert(self, node_val, prev_node_val):
        # check if no head, empty linked list.
        if not self.head:
            raise IndexError("Empty Linked List")
        # create a new Node
        new_node = Node(node_val)
        current = self.head
        # loop through the size of linked list to search for prev_node_val
        for _ in range(self.size):
            # if prev_node_val found
            if current.data == prev_node_val:
                # store the value of the next node
                next_node = current.next
                # check if value of the next node is not None
                if next_node:
                    # link the next node previous pointer to the new node
                    next_node.previous = new_node
                # check if value of the current node is not None
                if current:
                    current.next = new_node
                # set the next and previous pointers of the new node
                new_node.next = next_node
                new_node.previous = current

                # return a list of all values of the nodes
                n = self.head
                out = [n.data]
                for _ in range(self.size):
                    n = n.next
                    out.append(n.data)
                return out
            else:
                current = current.next
        # the prev_node_val was not found
        return f"{prev_node_val} is not a node"


newObj = DLinkedList()
newObj.append(12)
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
print(newObj.insert(100, 12))
