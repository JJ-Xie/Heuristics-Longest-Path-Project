#Stretches a graph into a tree by maximizing the increase of the periphery at the point with the lowest periphery
#Justin Xie

#Below is the Pseudocode for this heuristic

# To stretch the graph into a tree

# let n be the number of vertices, m be the number of edges


# for cut from m-(n-1)
#    target vertex = find vertex with lowest total periphery
#    if more than one vertex
#        target vertex = vertex with most neighbors

#    for all edges connected to target vertex
#        temporarily remove edge
#        calculate total periphery at vertex
#        if total periphery > highest periphery so far
#            higher periphery = total periphery
#            best edge = edge

#    cut edge from graph

import copy
import igraph as ig
from heuristics.dijkstras_longest_tree import dijkstras_tree


#Checks if graphs if connected by finding the number of clusters
def check_connection(graph):
    components = graph.clusters(mode='weak')
    if len(components) == 1:
        return True
    else:
        return False


def total_point_periphery(graph, vertex):
    total_periphery = 0

    #Loops through all neighbor vertices to find total of shortest paths to those vertices
    for other_vertex in graph.vs:
        if other_vertex == vertex:
            continue
        else:
            total_periphery += graph.shortest_paths(vertex, other_vertex)[0][0]

    return total_periphery


#Creates a dictionary mapping the vertices to their total periphery values
def total_periphery_mapping(graph):
    mapping = {}
    for i in range(len(graph.vs)):
        p = total_point_periphery(graph, i)
        mapping[i] = p
    
    return mapping


#Finds total periphery of a graph
def graph_total_periphery(graph):
    mapping = total_periphery_mapping(graph)
    total = 0
    for key in mapping.keys():
        total += mapping[key]
    return total


#Sorts all vertices based on their total periphery
def possible_source_vertices(graph, mapping):
    unsorted_possible = []
    for i in range(len(graph.vs)):
        unsorted_possible.append(i)
    sorted_possible = []

    #Compares each vertex to the previously sorted list
    #If a vertex has a lower periphery than sorted_possible[j], it is inserted in front
    #If two vertices have the same periphery, the one with more neighbors is place in front
    for vertex in unsorted_possible:
        if not sorted_possible:
            sorted_possible.append(vertex)
        else:
            for j in range(len(sorted_possible)):
                if mapping[vertex] < mapping[sorted_possible[j]]:
                    sorted_possible.insert(j, vertex)
                    break
                elif mapping[vertex] == mapping[sorted_possible[j]]:
                    if len(graph.neighbors(vertex)) > len(graph.neighbors(sorted_possible[j])):
                        sorted_possible.insert(j, vertex)
                        break
                    elif len(graph.neighbors(vertex)) == len(graph.neighbors(sorted_possible[j])):
                        sorted_possible.insert(j+1, vertex)
                        break
                if j == len(sorted_possible) - 1:
                    sorted_possible.append(vertex)

    return sorted_possible

#Finds the edge that maximizes the source vertex's total periphery
def find_best_edge(graph, source_vertices):

    #Loops through the source vertices until an edge can be removed without breaking connectivity
    for source in source_vertices:
        targets = graph.neighbors(source)
        best_target = None
        best_source_periphery = 0

        #Loops through the neighbors of the source vertex to find the one that maximizes the source vertex's total periphery
        #Ensures connectivity
        for target in targets:
            temp_g = copy.deepcopy(graph)
            temp_g.delete_edges([(source, target)])
            if check_connection(temp_g):
                p_periphery = total_point_periphery(temp_g, source)
                if p_periphery > best_source_periphery:
                    best_source_periphery = p_periphery
                    best_target = target

        #Finding a sufficient edge breaks the loop
        if best_target != None:
            the_source = source
            break
    edge = (the_source, best_target)

    return edge


#Cuts the graph into a tree by cutting the edge that maximizes the total periphery of the vertex with the lowest periphery
def stretch_node(graph):
    n = len(graph.vs)
    m = len(graph.es)

    #Cuts all excess edges not needed to form a tree
    for cut in range(m - (n-1)):
        mapping = total_periphery_mapping(graph)
        sources = possible_source_vertices(graph, mapping)
        edge = find_best_edge(graph, sources)
        graph.delete_edges([edge])

    return graph

def stretch_nodes_longest_path(graph):
    tree = stretch_node(graph)
    longest_path = dijkstras_tree(tree)
    return longest_path
