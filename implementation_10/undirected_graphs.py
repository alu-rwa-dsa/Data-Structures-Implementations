"""
Create an Undirected Weighted Graph class using Adjacency Matrices along with relevant primary methods.
 (Insert/Delete edge, Insert/Delete vertex/Update weight)
"""


class UndirectedGraph:
    def __init__(self):
        # self.v is a dictionary contains all of the vertex of the graph as keys and their indices as values
        # Ex: {"A": 0}
        self.v = {}
        # self.e is a V*V matrix that represents the all edges of the graph. An edge between two vertices is represented
        # by the weight of the edge and 0 if there is no edge.
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
            # check if weight value is not 0, return True
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

    def __verify_vertices(self, v1, v2):
        """
        __verify_vertices is a helper method takes in two vertices and verify v1 and v2 are existing vertices
        by raising an error if not.
        """

        if not self.isVertex(v1) or not self.isVertex(v2):
            raise KeyError('Vertex exist in the graph')

    def __update_edge_weight(self, v1, v2, w):
        """
        __update_edge is a helper method that is used to update the weight value of an existing edge
        """
        # verify that the weight is a numeric value
        if type(w) is not int:
            raise ValueError('weight should be int')
        v1_ind = self.v[v1]
        v2_ind = self.v[v2]
        self.e[v1_ind][v2_ind] = w
        self.e[v2_ind][v1_ind] = w
        return f"{v1} --- {v2} -- w = {w}"

    def insert_edge(self, v1, v2, w):
        """
        insert_edge takes in the name of two existing vertices (v1, v2) and connects them with the given weight, w.
            - Note: if v1 or v2 is not an existing vertex or there is an edge between v1 and v2 or weight is not int
                    value, an Error will be raised
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        self.__verify_vertices(v1, v2)
        # verify that there is no existing edge between v1 and v2
        if self.isEdge(v1, v2):
            raise KeyError('Edge exist between the two given vertices, you can only update the weight of their edge.')
        return self.__update_edge_weight(v1, v2, w)

    def delete_edge(self, v1, v2):
        """
        delete_edge takes in the name of two existing vertices (v1, v2) deletes the edge between them.
            - Note: if v1 or v2 is not an existing vertex or there is no edge between v1 and v2 an Error will be raised
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        self.__verify_vertices(v1, v2)
        # verify that there is an edge between v1 and v2
        if not self.isEdge(v1, v2):
            raise KeyError("Edge doesn't exist between the two given vertices")
        return self.__update_edge_weight(v1, v2, 0)

    def update_weight(self, v1, v2, new_weight):
        """
        delete_edge takes in the name of two existing vertices (v1, v2) and new weight to update the weight of the
        edge between them.
            - Note: if v1 or v2 is not an existing vertex or there is no edge between v1 and v2 or the new weight is
             not an numeric value, an Error will be raised.
        TimeComplexity: O(1)
        SpaceComplexity: O(1)
        """
        self.__verify_vertices(v1, v2)
        """
        TODO: do I need to check if the value of the current weight is 0, no edge, and raise an error?
        """
        return self.__update_edge_weight(v1, v2, new_weight)


graph = UndirectedGraph()
graph.insert_vertex("A")
graph.insert_vertex("B")
graph.insert_vertex("C")
graph.update_weight("A", "C")
