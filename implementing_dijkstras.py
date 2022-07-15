#Utilizes Dijkstra's Algorithm to find longest path in a tree with n nodes
#Justin Xie 

import igraph as ig

#A breadth first search algorithm to find one of the furthest nodes from a given nodes
def bfs(graph, start_node):
    output = []
    q = [start_node]
    available = set()
    for i in range(len(graph.vs)):
        available.add(i)
    available.remove(start_node)

    #Loops until queue is empty
    #For each item in the queue, the adjacent neighbors that have yet to be added are appended to the back of the queue
    #Each item is popped into the output list that represents the order the nodes were visited
    while q:
        current_node = q[0]
        adjacent = graph.neighbors(current_node)
        for node in adjacent:
            if node in available:
                q.append(node)
                available.remove(node)
        used_node = q.pop(0)
        output.append(used_node)
    return output[-1]


#Utilizing the breadth first search algorithm twice to find to extremes of the graph to find the longest path
def testing_dijkstras(graph):
        first = bfs(graph, 0)
        second = bfs(graph, first)
        longest_path = graph.shortest_paths(first, second)
        longest_path = longest_path[0][0] #Note: There is a double index as the shortest_paths function outputs a list inside of a list
        return longest_path