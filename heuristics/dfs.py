import igraph as ig
from matplotlib.style import available


#Takes in a graph and applies a DFS from a given starting node to all other available vertices
#Puts them in a graph
def dfs(visited, graph, node, dfs_graph): 
    if node not in visited:
        visited.add(node)
        for neighbour in graph.neighbors(node):
            if neighbour not in visited:
                dfs_graph.add_edge(node, neighbour)
                dfs_graph = dfs(visited, graph, neighbour, dfs_graph)
    return dfs_graph.simplify()


#Executes the graph DFS function on a give graph
#Ignores vertices that have been given as unavailable 
#Returns internal path length of DFS outputted graph
def execute_dfs(graph, start, visited, available):
    after_dfs = ig.Graph(directed=False)
    after_dfs.add_vertices(len(graph.vs))
    for i in range(len(after_dfs.vs)):
        after_dfs.vs[i]["id"]= i
        after_dfs.vs[i]["label"]= str(i)
    after_dfs = dfs(visited, graph, start, after_dfs)
    #ig.plot(after_dfs)
   
    #Calcualtes internal path length after each DFS
    #Finds highest internal path
    internal_path = 0
    for i in range(len(after_dfs.vs)):
        if i == start:
            continue
        elif i in available and len(after_dfs.neighbors(i)) > 0:
            #print(f'Node: {i}, shortest path: {after_dfs.get_shortest_paths(i, start)[0]}')
            #print(f'Node: {i}, distance: {len(after_dfs.get_shortest_paths(i, start)[0])}')
            internal_path += len(after_dfs.get_shortest_paths(i, start)[0]) - 1
    return internal_path
