import copy
from gettext import find
import igraph as ig
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path


def check_connection(graph):
    components = graph.clusters(mode='weak')
    if len(components) == 1:
        return True
    else:
        return False


#Finds the periphery of a vertex
def point_periphery(graph, vertex):
    periphery = 0

    #Loops through all 
    for i in range(len(graph.vs)):
        if i == vertex:
            continue
        else:
            shortest_path = graph.shortest_paths(vertex, i)[0][0]
            if  shortest_path > periphery:
                periphery = shortest_path
    return periphery


def total_periphery(graph):
    total = 0
    for i in range(len(g.vs)):
        p = point_periphery(graph, i)
        print(p)
        total += p
    
    return total


def periphery_mapping(graph):
    mapping = {}
    for i in range(len(graph.vs)):
        p = point_periphery(graph, i)
        mapping[i] = p
    
    return mapping


def from_vertex_prune(graph, mapping):
    unsorted_possible = []
    for i in range(len(g.vs)):
        unsorted_possible.append(i)
    sorted_possible = []

    for vertex in unsorted_possible:
        if not sorted_possible:
            sorted_possible.append(vertex)
        else:
            for j in range(len(sorted_possible)):
                if mapping[vertex] < mapping[sorted_possible[j]]:
                    sorted_possible.insert(j, vertex)
                    break
                elif mapping[vertex] == mapping[sorted_possible[j]]:
                    if len(graph.neighbors(vertex)) >= len(graph.neighbors(sorted_possible[j])):
                        sorted_possible.insert(j, vertex)
                        break
                if j == len(sorted_possible) - 1:
                    sorted_possible.append(vertex)
    return sorted_possible

def target_vertices_order(graph, mapping, originate_vertex):
    unsorted_possible = graph.neighbors(originate_vertex)
    sorted_possible = []

    for vertex in unsorted_possible:
        if not sorted_possible:
            sorted_possible.append(vertex)
        else:
            for j in range(len(sorted_possible)):
                if mapping[vertex] < mapping[sorted_possible[j]]:
                    sorted_possible.insert(j, vertex)
                    break
                elif mapping[vertex] == mapping[sorted_possible[j]]:
                    if len(graph.neighbors(vertex)) >= len(graph.neighbors(sorted_possible[j])):
                        sorted_possible.insert(j, vertex)
                        break
                if j == len(sorted_possible) - 1:
                    sorted_possible.append(vertex)

    return sorted_possible

def prune(graph, originate_vertex_order, mapping):
    for origin_vertex in originate_vertex_order:
        vertex_prune = origin_vertex
        option_order = target_vertices_order(graph, mapping, vertex_prune)
        cut = False
        
        for option in option_order:
            test_graph = copy.deepcopy(graph)
            edge_to_remove = (vertex_prune, option)
            test_graph.delete_edges([edge_to_remove])
            connected = check_connection(test_graph)
            if connected:
                #print(f'Cutting to target: {option}')
                graph.delete_edges([edge_to_remove])
                break
                cut = True
        if cut:
            break

def prune_graph(graph):
    for cuts in range(graph.ecount() - (len(g.vs) - 1)):
        p_mapping = periphery_mapping(graph)
        #print(p_mapping)
        originate_prune_order = from_vertex_prune(graph, p_mapping)
        #print(f'Originating Option Order {originate_prune_order}')
        prune(graph, originate_prune_order, p_mapping)


g = basetree_random_graph(7,9)

ig.plot(g)

prune_graph(g)
ig.plot(g)