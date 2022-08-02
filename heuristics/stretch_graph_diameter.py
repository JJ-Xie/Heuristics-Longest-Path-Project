# Turns a graph into a tree by maximizing the diameter of the graph
# Justin Xie 2022

import igraph as ig
import copy
from cmath import inf
from heuristics.dijkstras_longest_tree import dijkstras_tree


# Calculates the diameter of a graph 
# by comparing lengths of all shortest paths
def diameter(graph):
    dia = 0
    for i in graph.vs:
        for j in graph.vs:
            if i != j:
                shortest = graph.shortest_paths(i,j)[0][0]
                if shortest > dia:
                    dia = shortest
    return dia


# Stretches the graph into a tree by removing/cutting edges
# that maximize the diameter
def increase_diameter(graph):
    n = len(graph.vs)
    m = len(graph.es)

    # Loops through all cuts necessary to turn graph into tree
    for cut in range(m - (n-1)):
        best_edge = ()
        highest_diameter = 0
        # Loops through all edges and finds the one that increases
        # the diameter of the graph the most
        for e in graph.es:
            temp_g = copy.deepcopy(graph)
            temp_g.delete_edges(e.tuple)
            current_diameter = diameter(temp_g)
            if current_diameter > highest_diameter and current_diameter != inf:
                highest_diameter = current_diameter
                best_edge = e.tuple
        graph.delete_edges(best_edge)
    return graph


# Runs Dijkstras tree algorithm on the stretched diameter graph to find the longest path in the graph
def stretch_diameter_longest_path(graph):
    tree = increase_diameter(graph)
    longest_path = dijkstras_tree(tree)
    return longest_path