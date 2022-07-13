import igraph as ig

def greed(graph, vertex, available):
    best_option_stats = [0, 0]
    best_option = 0
    possibilities = graph.neighbors(vertex)
    for p in possibilities:
        if p in available:
            p_opp = len(graph.neighbors(p))
            if p_opp > best_option_stats[1]:
                best_option_stats = [p, p_opp]
    best_option = best_option_stats[0]
    if best_option_stats == [0,0]:
        return None
    else:
        return best_option

def greedy(graph):
    largest_path_length = 0
    for i in range(len(graph.vs)):
        current = i
        path_length = 0
        vertex_set = set()
        for j in range(len(graph.vs)):
            vertex_set.add(j)
        to_continue = True
        while to_continue:
            if current in vertex_set:
                vertex_set.remove(current)
                next = greed(graph, current, vertex_set)
                if next == None:
                    to_continue == False
                    break
                else:
                    path_length += 1
                    current = next
            else:
                to_continue = False
        if path_length > largest_path_length:
            largest_path_length = path_length
    return largest_path_length

def altruistic(graph, vertex, available):
    best_option_stats = [0, 0]
    best_option = 0
    possibilities = graph.neighbors(vertex)
    tracker = 0
    for p in possibilities:
        if p in available and len(graph.neighbors(p)) != 1:
            tracker += 1
            p_opp = len(graph.neighbors(p))
            if tracker == 1:
                best_option_stats = [p, p_opp]
            elif p_opp < best_option_stats[1]:
                best_option_stats = [p, p_opp]
    best_option = best_option_stats[0]
    if best_option_stats == [0,0]:
        for p in possibilities:
            if p in available:
                return p
    elif best_option_stats == [0,0]:
        return None
    else:
        return best_option

def altruism(graph):
    largest_path_length = 0
    for i in range(len(graph.vs)):
        current = i
        path_length = 0
        vertex_set = set()
        for j in range(len(graph.vs)):
            vertex_set.add(j)
        to_continue = True
        while to_continue:
            if current in vertex_set:
                vertex_set.remove(current)
                next = altruistic(graph, current, vertex_set)
                if next == None:
                    to_continue == False
                    break
                else:
                    path_length += 1
                    current = next
            else:
                to_continue = False
        if path_length > largest_path_length:
            largest_path_length = path_length
    return largest_path_length

def using_both(graph):
    greedy_approach = greedy(graph)
    altruistic_approach = altruism(graph)
    if greedy_approach > altruistic_approach:
        THE_longest_path = greedy_approach
    else:
        THE_longest_path = altruistic_approach
    return THE_longest_path