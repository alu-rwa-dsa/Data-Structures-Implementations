"""
Create an Undirected Weighted Graph class using Adjacency Matrices along with relevant primary methods.
 (Insert/Delete edge, Insert/Delete vertex/Update weight)
"""


class UndirectedGraph:
    def __init__(self):
        # self.v is a dictionary contains all of the vertex of the graph as keys and their index in
        # the edges list as value. Ex: {"A": 0}
        self.v = {}
        # self.e is a V*V matrix that represents the all edges of the graph. An edge between two vertices is represented
        # by the weight of the edge
        self.e = []

    def __str__(self):
        repre = ""
        for row in self.e:
            repre += str(row) + "\n"
        return repre

    def show_all_vertices(self):
        return list(self.v.keys())

    def isVertex(self, name):
        """
        isVertex takes in the name of a vertex and returns True if it exists in the graph and False otherwise
        TimeComplexity: O(1) since I am using a dictionary (hash map) which optimized the process of finding a vertex
        SpaceComplexity: O(1)
        """
        return name in self.v

    def isEdge(self, vertex_1, vertex_2):
        """
        isVertex takes in the two vertices and returns True if their is an edge between them, False otherwise
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        if self.isVertex(vertex_1) and self.isVertex(vertex_2):
            # verify that the index that represents the intersection between the vertices is not 0
            v1_ind = self.v[vertex_1]
            v2_ind = self.v[vertex_2]
            if self.e[v1_ind][v2_ind]:
                return True
        return False

    # insert a vertex
    def insert_vertex(self, name):
        """
        insert_vertex takes in the name of a new vertex and adds it to the graph.
            - Note: if there is a vertex with the same name, it will raise a keyError
        TimeComplexity: O(n) since we will have to loop through all of the existing row in the matrix to add
                        a new column for the new vertex
        SpaceComplexity: O(n)
        """
        if self.isVertex(name):
            raise KeyError('Vertex exist in the graph')
        nu_of_vertices = len(self.e)
        # store a new vertex in the vertices dictionary
        self.v[name] = nu_of_vertices
        # and a new column of zeros to represent the new vertex in the adjacency matrix
        for i in range(nu_of_vertices):
            self.e[i].append(0)
        # add a new row to represent the new vertex
        self.e.append([0] * (nu_of_vertices + 1))

    # delete a vertex
    def delete_vertex(self, vertex):
        """
        delete_vertex takes in a vertex name and deletes it from the adj matrix and the vertices dict
            - Note: if vertex doesn't exist in the graph, it will raise a keyError
        TimeComplexity: O(|v|) for looping through all elements of the adj matrix
        SpaceComplexity: O(|v|) for the worst case of deleting the first vertex which will lead to shifting all other
                         vertices in the adj list
        """
        # if the vertex doesn't exist in the graph
        if not self.isVertex(vertex):
            raise KeyError(f'{vertex} is not a Vertex')
        vertex_ind = self.v[vertex]

        # delete the vertex from the vertices dictionary
        del self.v[vertex]

        # delete the vertex row from the adj matrix
        self.e.pop(vertex_ind)

        # delete the connection between the vertex and all other vertices
        for v_edges in self.e:
            v_edges.pop(vertex_ind)

        # update the values of all existing vertices to match the new index of the adj matrix
        for key in self.v.keys():
            if self.v[key] > vertex_ind:
                self.v[key] -= 1
        return vertex

    def insert_edge(self, v1, v2, w):
        """
        insert_edge takes in the name of two existing vertices (v1, v2) and connects them with the given weight, w.
        """
        if not self.isVertex(v1) or not self.isVertex(v2):
            raise KeyError('Vertex exist in the graph')
        if self.isEdge(v1, v2):
            raise KeyError('Edge exist between the two given ')


graph = UndirectedGraph()
graph.insert_vertex("A")
graph.insert_vertex("B")
graph.insert_vertex("C")
