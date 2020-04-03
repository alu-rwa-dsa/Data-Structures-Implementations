import unittest  # import the unittest module to test the class methods

from implementation_7.linear_search import linearSearch


class TestSLinearSearch(unittest.TestCase):
    def test1(self):
        l = [1, 2, 3, 4, 5, 6]
        target = 4
        self.assertEqual(linearSearch(l, target), True)

    def test2(self):
        l = []
        target = 4
        self.assertEqual(linearSearch(l, target), False)

    def test3(self):
        l = [1, 2, 3, 4, 5, 6]
        target = 120
        self.assertEqual(linearSearch(l, target), False)

    def test4(self):
        l = [1, 2, 3, 4, 5, 6]
        target = 1
        self.assertEqual(linearSearch(l, target), True)


if __name__ == '__main__':
    unittest.main()
