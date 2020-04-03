import unittest  # import the unittest module to test the class methods

from implementation_6.det_mat import detMat


class TestDetOfMat(unittest.TestCase):
    def test1(self):
        self.assertEqual(detMat([[7, 2, 2, 1], [120, 1, 2, 3], [1, 1, 4, 8], [3, 4, 5, 6]]), -1056.0)

    def test2(self):
        self.assertEqual(detMat([[1, 2, 2], [1, 1, 1], [0, 3, 4]]), -1.0)

    def test3(self):
        self.assertEqual(detMat([[1, 2], [1, 1]]), -1.0)

    def test4(self):
        self.assertEqual(detMat([10]), 10)


if __name__ == '__main__':
    unittest.main()
