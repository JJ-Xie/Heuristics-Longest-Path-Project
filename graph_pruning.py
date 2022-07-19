import igraph as ig
from treestart_gen_random_graph import basetree_random_graph


def point_periphery(graph, vertex):
    periphery = 0
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
    vertex_to_be_pruned = 0
    lowest_periphery = 0
    tracker = 0
    
    for vertex in range(len(graph.vs)):
        if tracker == 0:
            vertex_to_be_pruned = vertex
            lowest_periphery = mapping[vertex]
            tracker += 1
        else:
            if mapping[vertex] < lowest_periphery:
                vertex_to_be_pruned = vertex
                lowest_periphery = mapping[vertex]
    
    return vertex_to_be_pruned
    

def to_vertex_prune(graph, mapping, options):
    vertex_to_be_pruned = 0
    lowest_periphery = 0
    tracker = 0

    for option in options:
        if tracker == 0:
            vertex_to_be_pruned = option
            lowest_periphery = mapping[option]
            tracker += 1
        else:
            if mapping[option] < lowest_periphery:
                vertex_to_be_pruned = option
                lowest_periphery = mapping[option]
    
    return vertex_to_be_pruned


def prune(graph, vertex_prune, mapping):
    options = graph.neighbors(vertex_prune)
    target_vertex_prune = to_vertex_prune(graph, mapping, options)
    print(target_vertex_prune)

    edge_to_remove = (vertex_prune, target_vertex_prune)
    graph.delete_edges([edge_to_remove])

    return graph


def prune_graph(graph):
    #for cuts in range(graph.edge_count - (len(g.vs) - 1)):
        p_mapping = periphery_mapping(graph)
        print(p_mapping)
        to_be_pruned = from_vertex_prune(graph, p_mapping)
        print(to_be_pruned)
        graph = prune(graph, to_be_pruned, p_mapping)
    
        return graph

g = basetree_random_graph(6,6)

graph = prune_graph(g)
