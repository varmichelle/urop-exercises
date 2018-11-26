INF = 99999

class Graph:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.matrix = matrix

def dijkstra(graph, source):
    # initialize distances array with matrix values
    distances = graph.matrix[source]
    visited = set()
    visited.add(source)
    
    for _ in range(graph.V - 1):
        u = 0
        dist = INF

        # find unvisited vertex with min distance
        for v in range(graph.V):
            if v not in visited and distances[v] < dist:
                dist = distances[v]
                u = v

        visited.add(u)

        # update distance matrix
        for v in range(graph.V):
            distances[v] = min(distances[v], distances[u] + graph.matrix[u][v])
    
    return distances

if __name__ == "__main__":
    # vertices numbered 0 to 8
    # edges from A to B given by graph[A][B] (adjacency matrix)
    matrix = [[0, 4, INF, INF, INF, INF, INF, 8, INF], 
              [4, 0, 8, INF, INF, INF, INF, 11, INF], 
              [INF, 8, 0, 7, INF, 4, INF, INF, 2], 
              [INF, INF, 7, 0, 9, 14, INF, INF, INF], 
              [INF, INF, INF, 9, 0, 10, INF, INF, INF], 
              [INF, INF, 4, 14, 10, 0, 2, INF, INF], 
              [INF, INF, INF, INF, INF, 2, 0, 1, 6], 
              [8, 11, INF, INF, INF, INF, 1, 0, 7], 
              [INF, INF, 2, INF, INF, INF, 6, 7, 0]]

    graph = Graph(9, matrix)
    distances = dijkstra(graph, 0)
    print(distances)