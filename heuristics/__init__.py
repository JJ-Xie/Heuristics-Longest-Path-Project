# Init file for calling heuristics
# Justin Xie 2022

from . import greedy, dfs_greedy, prune_central_edges, stretch_total_graph_periphery, stretch_lowest_node_periphery, stretch_graph_diameter

# Allows benchmark suite to call all functions 
# for comparison
all = [
    greedy.greedy_longest_path, 
    dfs_greedy.dfs_greedy_longest_path,
    prune_central_edges.prune_central_longest_path,
    stretch_total_graph_periphery.stretch_total_longest_path,
    stretch_lowest_node_periphery.stretch_nodes_longest_path,
    stretch_graph_diameter.stretch_diameter_longest_path
    ]


# Allows benchmark suite to call single functions
run_greedy = greedy.greedy_longest_path
run_dfs_greedy = dfs_greedy.dfs_greedy_longest_path
run_prune_central = prune_central_edges.prune_central_longest_path
run_stretch_total_graph = stretch_total_graph_periphery.stretch_total_longest_path
run_stretch_lowest_node = stretch_lowest_node_periphery.stretch_nodes_longest_path
run_stretch_diameter = stretch_graph_diameter.stretch_diameter_longest_path