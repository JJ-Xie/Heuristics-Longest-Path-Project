#Turning a graph into a tree by "stretching the string"
#Justin Xie 2022

#Below is the Pseudocode for this heuristic

# To stretch the graph into a tree

# let n be the number of vertices, m be the number of edges

# for cut from 0 to m-(n-1)
#    for all m edges
#        temporarily remove edge
#        find total periphery of graph
#        if total periphery > previous total periphery
#            highest total periphery = current total periphery
#            edge = edge to be cut
#    cut edge from graph

from cmath import inf
import copy
import igraph as ig
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path


#Finds the total periphery of a vertex by adding the shortest paths to all other nodes together
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


def graph_total_periphery(graph):
    mapping = total_periphery_mapping(graph)
    total = 0
    for key in mapping.keys():
        total += mapping[key]
    return total


def graph_stretching(graph):
    n = len(graph.vs)
    m = len(graph.es)
    for cut in range(m - (n-1)):
        best_edge = ()
        highest_total_periphery = 0
        for e in graph.es:
            temp_g = copy.deepcopy(graph)
            temp_g.delete_edges(e.tuple)
            current_total_periphery = graph_total_periphery(temp_g)
            if current_total_periphery > highest_total_periphery and current_total_periphery != inf:
                highest_total_periphery = current_total_periphery
                best_edge = e.tuple
        graph.delete_edges(best_edge)
    return graph

        