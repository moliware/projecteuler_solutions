# http://projecteuler.net/index.php?section=problems&id=18

# This problem is the same as shortest path problem in graph
# theory

import sys

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def bellman_ford(g, id):
    """ http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm """
    previous = {}
    lengths = dict.fromkeys(g.keys(), sys.maxint)
    lengths[id] = 0

    arcs = []
    for node1, adjacency in g.items():
        for node2 in adjacency.keys():
            arcs.append((node1,node2))
    
    for i in range(1, len(g) - 1):
        for u, v in arcs:
            if lengths[u] + g[u][v] < lengths[v]:
                lengths[v] = lengths[u] + g[u][v]
                previous[v] = u

    for u, v in arcs:
        if lengths[u] + g[u][v] < lengths[v]:
            raise Exception

    return previous, lengths

g = {}
node = 0
end_node = None
for i in range(len(triangle)):
    if i == len(triangle) - 1:
        # Create end node
        end_node = node + len(triangle[i])
        g[end_node] = {}
    for j in range(len(triangle[i])):
        g[node] = {} 
        # If we are in the last row of the triangle. Go to end node
        child = node + len(triangle[i]) if i != len(triangle) - 1 else end_node
        g[node][child] = triangle[i][j] * -1
        if not end_node:
            g[node][child + 1] = triangle[i][j] * -1
        node += 1
path, lengths = bellman_ford(g,0)
print lengths[end_node]*-1

