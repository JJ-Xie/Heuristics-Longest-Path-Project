# Finds longest path in an unconnected and unweighted graph
# Justin Xie 2022

import igraph as ig

# This function finds the longest simple path in a graph 
# by looping through a list of all simple paths  
def find_longest_path(g):
    paths_list = []
    longest = 0

    for i in range(len(g.vs)):
        paths_list = []
        paths_list = paths_list + g.get_all_simple_paths(g.vs[i]) #function from igraph
        longest_path = []
        for path in paths_list:
            if len(path) > longest:
                longest = len(path)
                longest_path = path

    if longest == 0:
        return None
    else:
        return longest - 1
