# http://projecteuler.net/index.php?section=problems&id=67

import sys
from urllib2 import urlopen

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

url = 'http://projecteuler.net/project/triangle.txt'
triangle = [map(int, line.split()) for line in urlopen(url).readlines()]


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
