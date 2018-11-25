def dijkstra(source, graph):
    distances = [99999]*8 # treat 99999 as INF
    distances[source] = 0
    return distances

if __name__ == "__main__":
    # vertices numbered 0 to 8
    # edges from A to B given by graph[A][B]
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
            [4, 0, 8, 0, 0, 0, 0, 11, 0], 
            [0, 8, 0, 7, 0, 4, 0, 0, 2], 
            [0, 0, 7, 0, 9, 14, 0, 0, 0], 
            [0, 0, 0, 9, 0, 10, 0, 0, 0], 
            [0, 0, 4, 14, 10, 0, 2, 0, 0], 
            [0, 0, 0, 0, 0, 2, 0, 1, 6], 
            [8, 11, 0, 0, 0, 0, 1, 0, 7], 
            [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    distances = dijkstra(0, graph)
    print(distances)