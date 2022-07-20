import copy
import igraph as ig
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path


#Checks if graphs if connected by finding the number of clusters
def check_connection(graph):
    components = graph.clusters(mode='weak')
    if len(components) == 1:
        return True
    else:
        return False


#Finds the periphery of a vertex
def point_periphery(graph, vertex):
    periphery = 0

    #Loops through all other vertices to find the longest shortest path which is the periphery
    for i in range(len(graph.vs)):
        if i == vertex:
            continue
        else:
            shortest_path = graph.shortest_paths(vertex, i)[0][0]
            if  shortest_path > periphery:
                periphery = shortest_path
    return periphery


#Finds the total periphery of the graph
def total_periphery(graph):
    total = 0
    for i in range(len(graph.vs)):
        p = point_periphery(graph, i)
        print(p)
        total += p
    
    return total


#Creates a dictionary with the keys being the vertices and the values being the periphery at that vertex 
def periphery_mapping(graph):
    mapping = {}
    for i in range(len(graph.vs)):
        p = point_periphery(graph, i)
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
        p_mapping = periphery_mapping(graph)
        source_prune_order = possible_source_vertices(graph, p_mapping)
        prune(graph, source_prune_order, p_mapping)
