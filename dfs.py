import igraph as ig

def dfs(visited, graph, node, dfs_graph): 
    if node not in visited:
        visited.add(node)
        for neighbour in graph.neighbors(node):
            if neighbour not in visited:
                dfs_graph.add_edge(node, neighbour)
                dfs_graph = dfs(visited, graph, neighbour, dfs_graph)
    return dfs_graph.simplify()


def execute_dfs(graph, start, visited, available):
    after_dfs = ig.Graph(directed=False)
    after_dfs.add_vertices(len(graph.vs))
    for i in range(len(after_dfs.vs)):
        after_dfs.vs[i]["id"]= i
        after_dfs.vs[i]["label"]= str(i)
    after_dfs = dfs(visited, graph, start, after_dfs)
   
    internal_path = 0
    for i in range(len(after_dfs.vs)):
        if i == start:
            continue
        elif i in available:
            internal_path += len(graph.get_shortest_paths(i, start)[0]) - 1
    return internal_path

        