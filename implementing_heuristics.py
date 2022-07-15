import igraph as ig

#Returns a list of nodes with the least connecting edges
def find_start_nodes(graph):
    start_nodes_list = []
    least_connections = 0
    for i in range(len(graph.vs)):
        if i == 0:
            least_connections = len(graph.neighbors(i))
            start_nodes_list.append(i)
        elif len(graph.neighbors(i)) < least_connections:
            least_connections = len(graph.neighbors(i))
            start_nodes_list = [i]
        elif len(graph.neighbors(i)) == least_connections:
            start_nodes_list.append(i)
    return start_nodes_list

#Returns a dictionary with keys representing the vertex and the label representing the number of connections it has (the score)
def gen_potential(graph):
    potential = {}
    for i in range(len(graph.vs)):
        potential[i] = len(graph.neighbors(i))
    return potential

#Returns a set containing all nodes from a graph
def gen_all_nodes_set(graph):
    all_nodes = set()
    for i in range(len(graph.vs)):
        all_nodes.add(i)
    return all_nodes

#Inputs a graph, a vertex, and the dictionary representing number of avaiable connections
#Returns the dictionary with the vertex key-value pair removed and the values of the nodes it was connected to are decremented by 1
def subtract_potential(graph, current_vertex, potential):
    all_neighbors = graph.neighbors(current_vertex)
    for i in range(len(all_neighbors)):
        if all_neighbors[i] in potential.keys():
            potential[all_neighbors[i]] -= 1
    potential.pop(current_vertex)
    return potential

#Inputs a graph, a vertex, a set of the available nodes, and the scores of each node
#Returns the "best" adjacent node to move to by finding the one with the lowest score
def best_next(graph, vertex, availability, potential):
    greatest_score = 0
    all_neighbors = graph.neighbors(vertex)
    tracker = 0
    next_candidate = None
    for i in range(len(all_neighbors)):
        if all_neighbors[i] in availability:
            node = all_neighbors[i]
            score = potential[node]
            if tracker == 0:
                greatest_score = score
                next_candidate = node
                tracker += 1
            else:
                if score < greatest_score and score != 0:
                    greatest_score = score
                    next_candidate = node
    #If all other options are gone, then the algorithm defaults to a node with zero next paths
    if next_candidate == None:
        for p in all_neighbors:
            if p in availability:
                return p
    else:
        return next_candidate

#Inputs a graph
#Returns the longest path in the graph
def altruist_longest_path(graph):
    longest_path_track = []
    longest_path_length = 0
    starting_nodes = find_start_nodes(graph)

    #Finds paths starting at the nodes with the least connections
    for i in range(len(starting_nodes)):
        path_tracker = []
        path_length = 0
        current = starting_nodes[i]
        potential = gen_potential(graph)
        available = gen_all_nodes_set(graph)
        to_continue = True
        while to_continue:
            path_tracker.append(current)
            potential = subtract_potential(graph, current, potential)
            next = best_next(graph, current, available, potential)
            if next == None:
                to_continue = False
                break
            else:
                available.remove(current)
                current = next
                path_length += 1
        if path_length > longest_path_length:
            longest_path_length = path_length
            longest_path_track = [path_tracker]
        elif path_length == longest_path_length:
            longest_path_track.append(path_tracker)
    return longest_path_length, longest_path_track