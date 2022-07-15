import igraph as ig
import random

#This function generates a random graph from a given number of vertices and edges
def unconnected_random_graph(n, m):

    #Creation of Graph
    g = ig.Graph(directed=False)
    g.add_vertices(n)

    #Continuously looping until the graph has the target number of edges and does not have any loops
    while g.ecount() < m or g != g.simplify():
        source = random.randint(0, n-1)
        target = random.randint(0, n-1)
        while target == source:
            target = random.randint(0,n-1)   
        g.add_edge(source, target)
    
    return(g)