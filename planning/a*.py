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
        cur_node = open[0]
        cur_index = 0
        for index, node in enumerate(open):
            if node.f < cur_node.f:
                cur_node = node
                cur_index = index

        open.pop(cur_index)
        closed.append(cur_node)

        # if we find the goal, return path
        if cur_node == E:
            path = []
            cur = cur_node
            while cur is not None:
                path.append(cur.pos)
                cur = cur.parent
            return path[::-1] # Return reversed path

        dir = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                dir.append((i,j))

        children = []

        for (dx, dy) in dir:
            pos = (cur_node.pos[0] + dx, cur_node.pos[1] + dy)
            if pos[0] >= len(grid) or pos[0] < 0 or pos[1] >= len(grid[0]) or pos[1] < 0:
                continue
            if grid[pos[0]][pos[1]] != 0:
                continue
            children.append(Node(cur_node, pos))

        for child in children:
            for closed_child in closed:
                if child == closed_child:
                    continue
            child.g = cur_node.g + 1
            child.h = ((child.pos[0] - E.pos[0]) ** 2) + ((child.pos[1] - E.pos[1]) ** 2)
            child.f = child.g + child.h
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