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
        return name in self.e

    def isEdge(self, start, end):
        if self.isVertex(start) and self.isVertex(end):
            return end in self.e[start]
        return False

    def __validate_vertex(self, vertex):
        if not self.isVertex(vertex):
            raise KeyError(f"{vertex} is not a vertex")

    def __validate_edge(self, start, end):
        if not self.isEdge(start, end):
            raise KeyError(f" No edge found between {start} and {end}")

    def show_edge(self, start=None, end=None):
        """
        show_edges takes in two optional parameter, start vertex and end vertex.
            - if start and end were given, it returns the edge between them
            - if start only, return all edges of it.
            - if None, return all vertices with their edges
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
        if not self.isVertex(name):
            self.e[name] = {}

    def delete_vertex(self, vertex):
        self.__validate_vertex(vertex)
        del self.e[vertex]
        return vertex

    def insert_edge(self, start, end, weight):
        """
        insert_edge takes in the start and end vertex with the weight of the edge
        Note: both vertices needs to be created first before adding an edge between them
        """
        self.__validate_vertex(start)
        self.__validate_vertex(end)
        weight_type = type(weight)
        # accept int values only for the weigh
        if weight_type is not int:
            raise ValueError(f"Weight should be of type int not {weight_type}")
        # check if the edge exists
        if self.isEdge(start, end):
            # if the weight is different, update the weight, otherwise raise a ValueError
            if weight == self.e[start][end]:
                raise ValueError('Edge exists')
            self.update_weight(start, end, weight)
        self.e[start][end] = weight
        return self.show_edge(start, end)

    def delete_edge(self, start, end):
        self.__validate_edge(start, end)
        del self.e[start][end]

    def update_weight(self, start, end, new_weight):
        self.__validate_edge(start, end)
        weight_type = type(new_weight)
        if weight_type is not int:
            raise ValueError(f"Weight should be of type int not {weight_type}")
        self.e[start][end] = new_weight
        return self.show_edge(start, end)


