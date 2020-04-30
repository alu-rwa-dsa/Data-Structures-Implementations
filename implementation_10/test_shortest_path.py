import unittest  # import the unittest module to test the class methods

from implementation_10.shortest_path import UndirectedGraph, findShortestLength2


class TestShortestPath(unittest.TestCase):
    def testShortestPath(self):
        g = UndirectedGraph()
        g.insert_vertex("A")
        g.insert_vertex("B")
        g.insert_vertex("C")
        g.insert_vertex("D")
        g.insert_edge("A", "B", 30)
        g.insert_edge("A", "C", 10)
        g.insert_edge("A", "D", 10)
        g.insert_edge("B", "C", 20)
        g.insert_edge("D", "C", 20)
        g.insert_edge("B", "D", 10)
        self.assertEqual(findShortestLength2(g), ['A', 'D', 'B'])

    def testShortestPath2(self):
        g = UndirectedGraph()
        g.insert_vertex("A")
        g.insert_vertex("B")
        g.insert_vertex("C")
        g.insert_vertex("D")
        g.insert_edge("A", "B", 30)
        g.insert_edge("A", "C", 10)
        g.insert_edge("A", "D", 10)
        g.insert_edge("B", "C", 20)
        self.assertEqual(findShortestLength2(g), ['C', 'A', 'D'])



if __name__ == '__main__':
    unittest.main()
