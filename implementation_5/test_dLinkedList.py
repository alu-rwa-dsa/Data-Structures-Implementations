import unittest  # import the unittest module to test the class methods

from implementation_5.doubly_linked_list import DLinkedList
from implementation_5.doubly_linked_list import Node


class TestSLinkedList(unittest.TestCase):
    def test_prepend(self):
        myObj = DLinkedList()  # initialize a new object of the class DLinkedList
        myObj.prepend(120)  # prepend a new value to the beginning of the linked list
        myObj.prepend(130)
        self.assertEqual(myObj.get_head(), 130)  # check the data in the head node
        self.assertEqual(myObj.get_tail(), 120)  # check the data in the tail node

    def test_pop_first(self):
        myObj = DLinkedList()
        myObj.prepend(120)
        myObj.prepend(130)
        self.assertEqual(myObj.pop_first(), 130)  # delete the head 130

    def test_append(self):
        myObj = DLinkedList()
        myObj.append(120)
        myObj.append(130)
        self.assertEqual(myObj.get_head(), 120)
        self.assertEqual(myObj.get_tail(), 130)

    def test_pop_last(self):
        myObj = DLinkedList()
        myObj.append(120)
        myObj.append(130)
        self.assertEqual(myObj.pop_last(), 130)  # delete the head 130

    def test_pop_last_2(self):
        """
        test deleting the last element from a non empty Linked List
        """
        myObj = DLinkedList()
        with self.assertRaises(IndexError):
            myObj.pop_last()

    def test_append_2(self):
        """
        Test the head and tail after appending one value only
        """
        myObj = DLinkedList()
        myObj.prepend(120)
        self.assertEqual(myObj.get_head(), 120)
        self.assertEqual(myObj.get_tail(), 120)

    def test_insert_node(self):
        """
        Test inserting a node to the Linked List giving the previous node
        """
        myObj = DLinkedList()
        myObj.append(120)
        myObj.append(100)
        self.assertEqual(myObj.insert_node(Node(1000), myObj.head), [120, 1000, 100])

    def test_delete_node(self):
        """
        Test deleting a node from the Linked List given the node
        """
        myObj = DLinkedList()
        myObj.append(120)
        myObj.append(100)
        myObj.detete_node(myObj.head.next)
        myObj.detete_node(myObj.head)
        self.assertEqual(myObj.get_head(), None)
        self.assertEqual(myObj.get_tail(), None)


if __name__ == '__main__':
    unittest.main()
