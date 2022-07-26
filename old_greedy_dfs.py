import igraph as ig
import dfs
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path

def tie_dfs(start_nodes, graph, availability):
    highest_internal = 0
    for start in start_nodes:
        visited = set()
        for i in range(len(graph.vs)):
            if i not in availability:
                visited.add(i)
        internal = dfs.execute_dfs(graph, start, visited, availability)
        if internal > highest_internal:
            highest_internal = internal
            best_node = start
    return best_node

def find_next(graph, vertex, available):
    best_nodes = []
    most_neighbors = 0
    tracker = 0
    for neighbor in graph.neighbors(vertex):
        if neighbor in available:
            nn = graph.neighbors(neighbor)
            if tracker == 0:
                best_nodes = [neighbor]
                most_neighbors = len(nn)
                tracker += 1
            else:
                if len(nn) < most_neighbors:
                    best_nodes = [neighbor]
                    most_neighbors = len(nn)
                elif len(nn) == most_neighbors:
                    best_nodes.append(neighbor)
    if not best_nodes:
        for anything in graph.neighbors(vertex):
            if anything in available:
                next_vertex = anything
            else:
                return None
    elif len(best_nodes) == 1:
        next_vertex = best_nodes[0]
    else:
        next_vertex = tie_dfs(best_nodes, graph, available)
    return next_vertex


def old_greedy(graph):
    longest_path_length = 0
    for start_vertex in range(len(graph.vs)):
        available = set()
        for i in range(len(graph.vs)):
            available.add(i)
        current = start_vertex
        to_continue = True
        path_tracker = []

        while to_continue:
            available.remove(current)
            path_tracker.append(current)
            next = find_next(graph, current, available)
            if next == None:
                to_continue = False
            current = next
        
        path_length = len(path_tracker)
        if path_length > longest_path_length:
            longest_path_length = path_length

    return longest_path_length - 1