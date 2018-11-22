class Vertex:
    def __init__(self, node):
        self.id = node
        self.paths = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.paths])

    def add_neighbor(self, neighbor, weight):
        self.paths[neighbor] = weight

    def get_paths(self):
        return self.paths.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.paths[neighbor]

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        self.vertices[node] = Vertex(node)

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, a, b, cost = 0):
        if a not in self.vertices:
            self.add_vertex(a)
        if b not in self.vertices:
            self.add_vertex(b)

        self.vertices[a].add_neighbor(self.vertices[b], cost)
        self.vertices[b].add_neighbor(self.vertices[a], cost)

    def get_vertices(self):
        return self.vertices.values()

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for vertex in g.get_vertices():
        print(vertex.__str__())