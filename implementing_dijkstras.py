#Utilizes Dijkstra's Algorithm to find longest path in a tree with n nodes
#Justin Xie 

import igraph as ig

def bfs(graph, start_node):
    output = []
    q = [start_node]
    available = set()
    for i in range(len(graph.vs)):
        available.add(i)
    available.remove(start_node)

    while q:
        current_node = q[0]
        adjacent = graph.neighbors(current_node)
        for node in adjacent:
            if node in available:
                q.append(node)
                available.remove(node)
        used_node = q.pop(0)
        output.append(used_node)
    return output[-1]

def testing_dijkstras(graph)
        first = bfs(graph, 0)
        second = bfs(graph, first)
        longest_path = graph.shortest_paths(first, second)
        longest_path = longest_path[0][0]
        return longest_path