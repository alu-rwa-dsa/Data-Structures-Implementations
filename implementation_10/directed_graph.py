"""
Create a Directed Weighted Graph class using Adjacency Lists along with the relevant primary methods.
(Insert/Delete edge, Insert/Delete vertex, Update weight)
"""


class DirectedGraph:
    def __init__(self):
        # e format {"vertex_0": {"vertex_1": weight}}, vertex_0 is connected to vertex_1
        self.e = {}

    def show_vertices(self):
        return list(self.e.keys())

    def show_edges(self, vertex=None):
        """
        show_edges takes in an optional parameter, vertex, to get all the vertices connected to it, otherwise get all
        edges.
        - If vertex was given and not found, a NameError error will be raised
        """
        if vertex:
            if vertex in self.e:
                return f"{vertex} -->> {self.e[vertex]}"
            else:
                raise KeyError(f"{vertex} is not a vertex")

        for v in self.e.keys():
            print(f"{v} -->> {self.e[vertex]}")

    def insert_vertex(self, name):
        if name in self.e:
            raise KeyError(f'{name} is an existing vertex')
        self.e[name] = {}
        return f"vertex {name} added successfully"

    def delete_vertex(self, name):
        if name not in self.e:
            raise KeyError(f"{name} is not a vertex")
        del self.e[name]
        return f"vertex {name} deleted successfully"

    def insert_edge(self, start, end, weight):
        """
        insert_edge takes in the start and end vertex with the weight of the edge
        Note: both vertices needs to be created first before adding an edge between them
        """
        if (start in self.e) and (end in self.e):
            self.e[start][end] = weight
            return "Edge added successfully"
        else:
            raise KeyError("vertices are not found")

    def delete_edge(self, start, end):
        if (start in self.e) and (end in self.e):
            if self.e[start][end]:
                del self.e[start][end]
            else:
                raise ValueError("Edge was not found")
        else:
            raise KeyError("vertices are not found")



# graph = DirectedGraph()
# graph.insert_vertex("A")
# graph.insert_vertex("B")
# graph.delete_vertex("A")
# print(graph.show_vertices())
# print(graph.show_edges("B"))
