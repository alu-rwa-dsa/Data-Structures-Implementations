"""
Create a Directed Weighted Graph class using Adjacency Lists along with the relevant primary methods.
(Insert/Delete edge, Insert/Delete vertex, Update weight)
"""


class DirectedGraph:
    def __init__(self):
        # e format {"vertex_0": {"vertex_1": weight}}, vertex_0 is connected to vertex_1
        self.e = {}

    def __repr__(self):
        """
        repr returns a list of all vertices in the graph
        """
        return str(list(self.e.keys()))

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

    def __validate_vertex(self, vertex):
        if not self.isVertex(vertex):
            raise KeyError(f"{vertex} is not a vertex")

    def __validate_edge(self, start, end):
        if not self.isDirectEdge(start, end):
            raise KeyError(f" No edge found between {start} and {end}")

    def show_edge(self, start=None, end=None):
        """
        show_edges takes in two optional parameter, start vertex and end vertex.
            - if start and end were given, it returns the edge between them
            - if start only, return all edges of it.
            - if None, return all vertices with their edges

        TimeComplexity: If start and/ or end is given O(1), otherwise O(|v|) where |v| is the number of vertices
        SpaceComplexity: O(1)
        """
        if start:
            self.__validate_vertex(start)
        if end:
            self.__validate_vertex(end)
        if start and end:
            self.__validate_edge(start, end)
            return f"{start} -->> {end} -->> {self.e[start][end]}"
        elif start:
            return f"{start} -->> {self.e[start]}"
        # if not start nor end were given
        for v in self.e.keys():
            print(f"{v} -->> {self.e[v]}")

    def insert_vertex(self, name):
        """
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        if not self.isVertex(name):
            self.e[name] = {}

    def delete_vertex(self, vertex):
        """
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        self.__validate_vertex(vertex)
        del self.e[vertex]
        return vertex

    def insert_edge(self, start, end, weight):
        """
        insert_edge takes in the start and end vertex with the weight of the edge
        Note: both vertices needs to be created first before adding an edge between them
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        self.__validate_vertex(start)
        self.__validate_vertex(end)
        weight_type = type(weight)
        # accept int values only for the weigh
        if weight_type is not int:
            raise ValueError(f"Weight should be of type int not {weight_type}")
        # check if the edge exists
        if self.isDirectEdge(start, end):
            # if the weight is different, update the weight, otherwise raise a ValueError
            if weight == self.e[start][end]:
                raise ValueError('Edge exists')
            self.update_weight(start, end, weight)
        self.e[start][end] = weight
        return self.show_edge(start, end)

    def delete_edge(self, start, end):
        """
        TimeComplexity: O(1) since finding the element is O(1)
        SpaceComplexity: O(1)
        """
        self.__validate_edge(start, end)
        del self.e[start][end]

    def update_weight(self, start, end, new_weight):
        """
        TimeComplexity: O(1) since finding the element is O(1)
        SpaceComplexity: O(1)
        """
        self.__validate_edge(start, end)
        weight_type = type(new_weight)
        if weight_type is not int:
            raise ValueError(f"Weight should be of type int not {weight_type}")
        self.e[start][end] = new_weight
        return self.show_edge(start, end)

    def FindPath(self, start, end):
        """
        FindPath(v1,v2) takes in the a start and end vertices and finds a path from v1 to v2. It returns an array.
        The output is an array of edges starting from v1 and ending at v2 such that there is a directed
        edge from v1 to the next and so on until v2 or returns False if no path exists.

        Implemented using DFS
        TimeComplexity: O(|V| + |E|)
        SpaceComplexity: O(|v|) where is the number of vertices
        """
        self.__validate_vertex(start)
        self.__validate_vertex(end)
        stack = [start]
        seen = {start}
        return self.__helper(stack, seen, end)

    def __helper(self, stack, seen, end):
        # base_case_1: when the stack is empty, return False, there is no such path
        if not stack:
            return False
        # base_case_2: the last element of the stack is the destination vertex
        if stack[-1] == end:
            return stack
        for vertex in self.e[stack[-1]].keys():
            if vertex not in seen:
                stack.append(vertex[0])
                seen.add(vertex[0])
                return self.__helper(stack, seen, end)
        # in case the vertex doesn't have any edges, pop the element from the stack
        stack.pop()
        return self.__helper(stack, seen, end)


g = DirectedGraph()
g.insert_vertex("A")
g.insert_vertex("B")
g.insert_vertex("D")
g.insert_vertex("C")
g.insert_edge("A", "B", 120)
g.insert_edge("A", "D", 100)
g.insert_edge("D", "C", 100)
print(g.FindPath("A", "C"))



