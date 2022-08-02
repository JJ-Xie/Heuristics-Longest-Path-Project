#Visualizes the total periphery of all vertices in a graph
#Justin Xie 2022

import igraph as ig
from treestart_gen_random_graph import basetree_random_graph

#Calculates the total periphery at a point
def total_point_periphery(graph, vertex):
    total_periphery = 0

    for other_vertex in graph.vs:
        total_periphery += graph.shortest_paths(vertex, other_vertex)[0][0]

    return total_periphery

#Maps each vertex to its total periphery
def total_periphery_mapping(graph):
    mapping = {}
    for i in range(len(graph.vs)):
        p = total_point_periphery(graph, i)
        mapping[i] = p
    
    return mapping


#Assigns a color gradient the sorted unique total periphery values 
def color_assignment(graph, mapping):
    
    #Creates a unique list of total periphery values
    unique = set()
    for p in mapping.values():
        unique.add(p)
    unique = sorted(list(unique))
    
    #Creates a gradient and assigns each unique periphery a color
    #More yellow equals lower periphery
    #More red equals higher periphery
    color_assign = {}
    pal = ig.GradientPalette("yellow", "red", len(unique))
    for i in range(len(unique)):
        color_assign[unique[i]] = pal.get(i)
    
    return color_assign


#Assigns vertices their colors based on the gradient mapping
def vertex_color_assignment(graph, mapping, color_mapping):
    for i in range(len(graph.vs)):
        i_periphery = mapping[i]
        graph.vs[i]["color"] = color_mapping[i_periphery]
    return graph


if __name__ == "__main__":
    g = basetree_random_graph(14, 22)

    mapping = total_periphery_mapping(g)
    color_mapping = color_assignment(g, mapping)
    g = vertex_color_assignment(g, mapping, color_mapping)

    ig.plot(g)