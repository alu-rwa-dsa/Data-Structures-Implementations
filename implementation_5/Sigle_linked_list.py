class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SLinkedList:
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

    def get_next(self):
        if self.head is None:
            return None
        return self.head.next.data

    def get_size(self):
        return self.size

    def prepend(self, val):
        temp = self.head
        newNode = Node(val)
        newNode.next = temp
        if self.tail is None:
            self.tail = newNode
        self.head = newNode
        self.size += 1

    def pop_first(self):
        if self.head is None:
            raise IndexError
        else:
            del_val = self.head.data
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
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
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_last(self):
        if self.head is None:
            return None
        last_node = self.tail.data
        current = self.head
        temp = None
        while current.next:
            temp = current
            current = current.next
        self.tail = temp
        if self.tail:
            self.tail.next = None
        self.size -= 1
        if self.size == 0:
            self.head = None
        return last_node


# myObj = SLinkedList()
# myObj.prepend(120)
# myObj.prepend(130)
# print(myObj.get_head())
# print(myObj.get_next())
# myObj.pop_first()
# print(myObj.get_head())
# myObj.append(1000)
# print(myObj.get_tail())
# print(myObj.get_head())
# print(myObj.pop())
# print(myObj.get_size())
# print(myObj.pop_last())
# print(myObj.get_size())
# print(myObj.get_tail())
# print(myObj.get_head())
# print(myObj.pop_last())

myObj = SLinkedList()
myObj.append(120)
myObj.append(130)
print(myObj.get_head())
print(myObj.get_next())







