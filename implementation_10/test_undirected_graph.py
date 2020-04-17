import unittest  # import the unittest module to test the class methods

from implementation_10.undirected_graphs import UndirectedGraph


class TestUndirectedGraph(unittest.TestCase):
    def testIsVertex(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        self.assertEqual(graph.isVertex("A"), True)
        self.assertEqual(graph.isVertex("C"), False)

    def testIsEdge(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        self.assertEqual(graph.isEdge("A", "D"), True)
        self.assertEqual(graph.isEdge("A", "K"), False)

    def testUpdateWeight(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        self.assertEqual(graph.update_weight("A", "D", 1200), "A --- D --- 1200")

    def testUpdateWeightOfNonExistingVertices(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        with self.assertRaises(KeyError):
            graph.update_weight("A", "K", 1200)

    def testRemoveVertex(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.delete_vertex("A")
        self.assertEqual(graph.isVertex("A"), False)

    def testRemoveEdge(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        graph.delete_edge("A", "D")
        self.assertEqual(graph.isEdge("A", "D"), False)
        # test deleting non-existing edge
        with self.assertRaises(KeyError):
            graph.delete_edge("A", "D")

    def testInsertAnExistingEdge(self):
        graph = UndirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        with self.assertRaises(KeyError):
            # insert the same edge with its previous weight
            graph.insert_edge("A", "D", 100)


if __name__ == '__main__':
    unittest.main()
