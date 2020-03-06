import unittest  # import the unittest module to test the class methods

from find_gcd import gcd


class TestSLinkedList(unittest.TestCase):
    def test1(self):
        self.assertEqual(gcd(20, 30), 10)

    def test2(self):
        self.assertEqual(gcd(0, 0), 0)

    def test3(self):
        self.assertEqual(gcd(270, 192), 6)

    def test4(self):
        self.assertEqual(gcd(300, 1000), 100)


if __name__ == '__main__':
    unittest.main()
