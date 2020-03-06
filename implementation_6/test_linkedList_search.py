"""
Please find the code in Implementation 5 folder, single_linked_list.py
"""

import unittest  # import the unittest module to test the class methods

from implementation_5.single_linked_list import SLinkedList


class TestSLinkedList(unittest.TestCase):
    def test1(self):
        newObj = SLinkedList()
        newObj.prepend(10)
        newObj.prepend(20)
        newObj.prepend(120)
        self.assertEqual(newObj.search(10), True)

    def test2(self):
        newObj = SLinkedList()
        newObj.prepend(10)
        newObj.prepend(20)
        newObj.prepend(120)
        self.assertEqual(newObj.search("ahmed"), False)

    def test3(self):
        newObj = SLinkedList()
        newObj.prepend(10)
        newObj.prepend(20)
        newObj.prepend(120)
        self.assertEqual(newObj.search(500), False)

    def test4(self):
        newObj = SLinkedList()
        self.assertEqual(newObj.search(10), False)

if __name__ == '__main__':
    unittest.main()
