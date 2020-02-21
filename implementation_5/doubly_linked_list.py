class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.previous = None


class DLinkedList:
    """
    DLinkedList class contains the main methods of a doubly linked list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_head(self):
        """
        get the value of the first node
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
        if self.head is None:
            return None
        return self.head.data

    def get_tail(self):
        """
        get the value of the last node
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
        if self.tail is None:
            return None
        return self.tail.data

    def get_size(self):
        return self.size

    def prepend(self, val):
        """
        add a leading node at the beginning of the linked list giving its value
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
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
        """
        delete the leading node of the linked list
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
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
        """
        add a node at the end of the linked list giving its value
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
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
        """
        delete the last node of the linked list
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
        if self.head is None:
            raise IndexError
        last_node = self.tail.data
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        self.size -= 1
        if self.size == 0:
            self.head = None
        return last_node

    def insert_node(self, new_node, previous_node):
        """
        insert a giving node to the new list given the previous node to it
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
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
        out = [n.data]
        for _ in range(self.size):
            n = n.next
            out.append(n.data)
        return out

    def detete_node(self, node):
        """
        delete a given node
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
        prev_node = node.previous  # get the node before the node to delete
        next_node = node.next  # get the node after the node to delete
        if (not prev_node) and (not next_node):  # if there are nodes before and after the node (linked list size is 1)
            self.head = None  # set the head to None
            self.tail = None  # set the tail to None
        if prev_node:  # if previous node found
            prev_node.next = next_node  # set its next reference to the next node
        else:
            self.head = next_node  # if not found, set head of the linked list to the next node
        if next_node:
            next_node.previous = prev_node
        else:
            self.tail = prev_node



