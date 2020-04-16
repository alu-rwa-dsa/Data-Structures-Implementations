import unittest  # import the unittest module to test the class methods

from implementation_10.directed_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):
    def testIsVertex(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        self.assertEqual(graph.isVertex("A"), True)
        self.assertEqual(graph.isVertex("C"), False)

    def testIsEdge(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        self.assertEqual(graph.isEdge("A", "D"), True)
        self.assertEqual(graph.isEdge("A", "K"), False)

    def testUpdateWeight(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        self.assertEqual(graph.update_weight("A", "D", 1200), "A -->> D -->> 1200")

    def testUpdateWeightOfNonExistingEdge(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        with self.assertRaises(KeyError):
            graph.update_weight("K", "D", 1200)

    def testRemoveVertex(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.delete_vertex("A")
        self.assertEqual(graph.isVertex("A"), False)

    def testRemoveEdge(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        graph.delete_edge("A", "D")
        self.assertEqual(graph.isEdge("A", "D"), False)

    def testInsertAnExistingEdge(self):
        graph = DirectedGraph()
        graph.insert_vertex("A")
        graph.insert_vertex("D")
        graph.insert_edge("A", "D", 100)
        with self.assertRaises(ValueError):
            # insert the same edge with its previous weight
            graph.insert_edge("A", "D", 100)

        # insert the same edge with a different weight leads to updating the weight
        self.assertEqual(graph.insert_edge("A", "D", 200), "A -->> D -->> 200")


if __name__ == '__main__':
    unittest.main()
