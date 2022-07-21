#Cuts a graph into a tree
#Justin Xie 2022

import copy
import igraph as ig
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path

#Below is the PseudoCode for this heuristic:

# To prune the "shortcuts" from a graph and turn it into a tree

# let n be the number of nodes, m be the number of edges

# for cut from 0 to the m - (n-1)

#    map each vertex to its total periphery
#    source_vertices = sort vertices by lowest to highest total periphery

#    for source_vertex in source_vertices
#        target_vertices = sort neighboring vertices by lowest to highest total periphery

#        for target_vertex in target_vertices
#            edge = source_vertex to target_vertex
#            if graph is connected when edge is removed
#                move to next cut
#            else
#                next edge


#Checks if graphs if connected by finding the number of clusters
def check_connection(graph):
    components = graph.clusters(mode='weak')
    if len(components) == 1:
        return True
    else:
        return False

#Finds the total periphery of a vertex by adding the shortest paths to all other nodes together
def total_point_periphery(graph, vertex):
    total_periphery = 0

    #Loops through all neighbor vertices to find total of shortest paths to those vertices
    for other_vertex in graph.vs:
        total_periphery += graph.shortest_paths(vertex, other_vertex)[0][0]

    return total_periphery


#Creates a dictionary mapping the vertices to their total periphery values
def total_periphery_mapping(graph):
    mapping = {}
    for i in range(len(graph.vs)):
        p = total_point_periphery(graph, i)
        mapping[i] = p
    
    return mapping


#Sorts the of a graph from lowest to highest periphery
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


#Sorts the list of neighbors connected to the source vertex
def target_vertices_order(graph, mapping, source_vertex):
    unsorted_possible = graph.neighbors(source_vertex)
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


#Cuts one edge from the inputted graph based on provided source and target vertices
def prune(graph, originate_vertex_order, mapping):

    #Loops through the sorted list of source vertices
    for origin_vertex in originate_vertex_order:
        vertex_prune = origin_vertex
        option_order = target_vertices_order(graph, mapping, vertex_prune)
        cut = False
        
        #For each source vertex, the function loops through the sorted list of available target vertices
        for option in option_order:
            test_graph = copy.deepcopy(graph)
            edge_to_remove = (vertex_prune, option)
            test_graph.delete_edges([edge_to_remove])
            connected = check_connection(test_graph)

            #If the graph is connected when cut, both loops are broken as the function has successfully removed an edge
            #Ensures the graph is still connected
            if connected:
                graph.delete_edges([edge_to_remove])
                cut = True
                break
        if cut:
            break


#Executes the number of pruning steps needed to convert the graph into a tree
#Prunes so the Dijkstra longest path in a tree algorithm can work
def prune_graph(graph):
    for cuts in range(graph.ecount() - (len(graph.vs) - 1)):
        p_mapping = total_periphery_mapping(graph)
        source_prune_order = possible_source_vertices(graph, p_mapping)
        prune(graph, source_prune_order, p_mapping)
