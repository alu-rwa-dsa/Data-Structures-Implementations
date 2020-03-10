class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SLinkedList:
    """
    SLinkedList class contains the main methods of a single linked list
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
        if self.head is None:  # check for a head node in the linked list
            return None  # return None if there are no nodes in the linked list
        return self.head.data  # if first node found, return its data

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
        temp = self.head  # store the current head
        newNode = Node(val)  # create a new node with the giving value
        newNode.next = temp  # set the reference of the new node to the current head
        if self.tail is None:  # check if linked list is empty
            self.tail = newNode  # if empty, set the tail to the new node
        self.head = newNode  # set the head to the new node
        self.size += 1  # increase the number of elements of the list

    def pop_first(self):
        """
        delete the leading node of the linked list
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
        if self.head is None:  # check if linked list is empty
            raise IndexError  # raise an index error
        else:
            del_val = self.head.data  # store the value of the leading node to return it
            new_head = self.head.next  # get the node after the head
            self.head.next = None  # delete the reference of the current head by sitting it to None
            self.head = new_head  # set the new head
            self.size -= 1  # decrease the number of elements in the linked list by 1
            if self.size == 0:  # check the size of the linked list after deleting the leading node
                self.tail = None  # if empty, set tail to None
            return del_val

    def append(self, val):
        """
        add a node at the end of the linked list giving its value
        """
        # Time complexity: O(1)
        # Space complexity: O(1)
        new_node = Node(val)
        if self.head is None:  # check if the linked list is empty, if yes, set the head and tail to the new node
            self.tail = new_node
            self.head = new_node
        else:  # if no, set the current tail to the new added node and set the new node as a tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_last(self):
        """
        delete the last node of the linked list
        """
        # Time complexity: O(n) because we need to reach the last node before the tail
        # Space complexity: O(1)
        if self.head is None:  # check if the linked list is empty, if yes, raise an Index error
            raise IndexError
        last_node = self.tail.data  # get the data of the last node to return it as output of the operation
        current = self.head
        temp = None
        while current.next:  # loop till the pointer reaches the last node before the tail
            temp = current
            current = current.next
        self.tail = temp  # set the last value before the tail as a new tail
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        return last_node

    def search(self, val):
        """
        check if a value is in the current LinkedList
        TimeComplexity: O(n) since we will loop through the whole LinkedList in the worst case when the val is not
        found
        SpaceComplexity: O(1) since no extra space needed
        """
        # check if the current node is None (next.tail)
        if self.head is None:
            return False
        # check if the date in the current node is equals to the given val
        if self.head.data == val:
            return True
        # move the head to the next node
        self.head = self.head.next
        # call the search function recursively
        return self.search(val)

