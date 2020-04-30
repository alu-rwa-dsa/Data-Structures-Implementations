class UndirectedGraph:
    """
    Direct Graph using Adjacency matrix
    """

    def __init__(self):
        # e format {"vertex_0": {"vertex_1": weight}}, vertex_0 is connected to vertex_1
        self.e = {}

    def show_graph(self):
        for key in self.e.keys():
            print(f"{key}: {self.e[key]}")

    def isVertex(self, name):
        """
        TimeComplexity: O(1) since I am using a dictionary (hash map) which optimized the process of finding a vertex
        SpaceComplexity: O(1)
        """
        return name in self.e

    def isDirectEdge(self, start, end):
        """
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        if self.isVertex(start) and self.isVertex(end):
            return end in self.e[start]
        return False

    def insert_vertex(self, name):
        """
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        if not self.isVertex(name):
            self.e[name] = {}

    def delete_vertex(self, vertex):
        """
        TimeComplexity: O(n)
        SpaceComplexity: O(1)
        """
        if not self.isVertex(vertex):
            raise ValueError("vertex doesn't exisit")
        del self.e[vertex]
        for k in self.e.keys():
            if vertex in self.e[k]:
                del self.e[k][vertex]
        return vertex

    def insert_edge(self, start, end, weight):
        """
        insert_edge takes in the start and end vertex with the weight of the edge
        Note: both vertices needs to be created first before adding an edge between them
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        if not self.isVertex(start):
            self.insert_vertex(start)
        if not self.isVertex(end):
            self.insert_vertex(end)
        weight_type = type(weight)
        # accept int values only for the weigh
        if weight_type is not int:
            raise ValueError(f"Weight should be of type int not {weight_type}")
        self.e[start][end] = weight
        self.e[end][start] = weight

    def delete_edge(self, start, end):
        """
        TimeComplexity: O(1) since finding the element is O(1)
        SpaceComplexity: O(1)
        """
        if not self.isDirectEdge(start, end):
            raise KeyError("edge doesn't exist in the graph")
        w = self.e[start][end]
        del self.e[start][end]
        del self.e[end][start]
        return w


    def update_weight(self, start, end, new_weight):
        """
        TimeComplexity: O(1) since finding the element is O(1)
        SpaceComplexity: O(1)
        """
        if not self.isDirectEdge(start, end):
            raise KeyError("edge doesn't exist in the graph")
        weight_type = type(new_weight)
        if weight_type is not int:
            raise ValueError(f"Weight should be of type int not {weight_type}")
        self.e[start][end] = new_weight
        self.e[end][start] = new_weight


def FindShortestLength2(graph):
    """
    FindShortestLength2(UWG) takes an Undirected Weighted Graph as input and finds the shortest
     (in terms of sums of the weight) path of length 2 outputting the 3 vertices that form the path of length 2.
      Edges may not be repeated in the path.
    """
    out = []
    min_so_far = 99999
    seen = set()
    for key, value in graph.e.items():
        # loop through the elements of the key
        for k, v in value.items():
            for k1, v1 in graph.e[k].items():
                path = [key, k, k1]
                path_str = "".join(path)
                if (k1 == key) or (path_str in seen):
                    continue
                seen.add(path_str)
                c_sum = v + v1
                if c_sum < min_so_far:
                    min_so_far = c_sum
                    out = [key, k, k1]
    return out

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
print(FindShortestLength2(g))