import unittest  # import the unittest module to test the class methods

from implementation_5.single_linked_list import SLinkedList


class TestSLinkedList(unittest.TestCase):
    def test_prepend(self):
        myObj = SLinkedList()
        myObj.prepend(120)
        myObj.prepend(130)
        self.assertEqual(myObj.get_head(), 130)
        self.assertEqual(myObj.get_tail(), 120)

    def test_pop_first(self):
        myObj = SLinkedList()
        myObj.prepend(120)
        myObj.prepend(130)
        self.assertEqual(myObj.pop_first(), 130)  # delete the head 130

    def test_append(self):
        myObj = SLinkedList()
        myObj.append(120)
        myObj.append(130)
        self.assertEqual(myObj.get_head(), 120)
        self.assertEqual(myObj.get_tail(), 130)

    def test_pop_last(self):
        myObj = SLinkedList()
        myObj.append(120)
        myObj.append(130)
        self.assertEqual(myObj.pop_last(), 130)  # delete the head 130

    def test_pop_last_2(self):
        """
        test deleting the last element from a non empty Linked List
        """
        myObj = SLinkedList()
        with self.assertRaises(IndexError):
            myObj.pop_last()

    def test_pop_last_3(self):
        """
        test tail and head if all elements are deleted
        """
        myObj = SLinkedList()
        myObj.append(120)
        myObj.append(130)
        myObj.pop_last()
        myObj.pop_last()
        self.assertEqual(myObj.get_tail(), None)

    def test_append_2(self):
        """
        Test the head and tail after appending one value only
        """
        myObj = SLinkedList()
        myObj.prepend(120)
        self.assertEqual(myObj.get_head(), 120)
        self.assertEqual(myObj.get_tail(), 120)


if __name__ == '__main__':
    unittest.main()
