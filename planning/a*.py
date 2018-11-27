class Node():

    def __init__(self, parent, pos):
        self.parent = parent
        self.pos = pos
        self.g, self.h, self.f = (0,0,0)

    def __eq__(self, other):
        return self.pos == other.pos

def a_star(grid, start, end):

    S = Node(None, start)
    S.g = S.h = S.f = 0
    E = Node(None, end)
    E.g = E.h = E.f = 0

    open = [S]
    closed = []

    while len(open) > 0:

        # find node with lowest cost
        cur = open[0]
        index = 0
        for i, node in enumerate(open):
            if node.f < cur.f:
                cur = node
                index = i

        open.pop(index)
        closed.append(cur)

        # if we find the goal, return path
        if cur == E:
            path = []
            cur = cur
            while cur is not None:
                path.append(cur.pos)
                cur = cur.parent
            path.reverse() # reverse because the path was constructed backwards
            return path

        # neighbors = all adjacent nodes (including diagonals)
        dir = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                dir.append((i,j))

        # append all neighbors
        for (dx, dy) in dir:
            pos = (cur.pos[0] + dx, cur.pos[1] + dy)
            if pos[0] >= len(grid) or pos[0] < 0 or pos[1] >= len(grid[0]) or pos[1] < 0:
                continue
            if grid[pos[0]][pos[1]] != 0:
                continue
            child = Node(cur, pos)
            if child in closed:
                continue
            child.g += 1 # one step farther away from origin
            child.h = ((child.pos[0] - E.pos[0]) ** 2) + ((child.pos[1] - E.pos[1]) ** 2) # Euclidean heuristic
            child.f = child.g + child.h

            # append child if it either hasn't been visited or has a lower cost than previously
            for open_node in open:
                if child == open_node and child.g > open_node.g:
                    continue
            open.append(child)

if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)
    path = a_star(grid, start, end)
    print(path)