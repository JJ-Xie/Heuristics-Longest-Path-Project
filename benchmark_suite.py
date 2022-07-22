# Longest path heuristic benchmarking.
# Justin Xie 2022

# This code benchmarks various longest-path heuristics for
# path quality and performance.

import igraph as ig
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path
from implementing_heuristics import altruist_longest_path
from graph_pruning_most_central import prune_graph_longest_path
from stretch_total_graph import graph_stretching_longest_path
from stretch_lowest_node import stretch_nodes_longest_path

def print_base_stats(heuristic, n, m, runs):
    print(f"Heurisic: {heuristic.__name__}")
    print(f"Nodes: {n}")
    print(f"Edges: {m}")
    print(f"Runs: {runs}")


# Benchmarks how well a heuristic outputs the exact longest
# path.
def complete_accuracy(n, m, heuristic, runs):
    accurate = 0
    for run in range(runs):
        g = basetree_random_graph(n, m)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        if actual_lp == heuristic_lp:
            accurate += 1
    accuracy_rate = round(accurate / runs * 100, 2)
    print("---- Complete Accuracy Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Accuracy Rate: {accuracy_rate}")
    return accuracy_rate


# Benchmarks how far off a function is from the actual
# longest path.
def error_accuracy(n, m, heuristic, runs):
    total_difference = 0
    for run in range(runs):
        g = basetree_random_graph(n, m)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        accuracy_diffference = actual_lp - heuristic_lp
        total_difference += accuracy_diffference
    average_difference = round(total_difference / runs, 2)
    print("---- Error Accuracy Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Average Error: {average_difference}")
    return average_difference


# Finds the number of and plots the graphs that cause the
# heuristic to fail to find the correct longest path
def find_heuristic_fail(n, m, heuristic, runs):
    failed_graphs = []
    for run in range(runs):
        g = basetree_random_graph(n, m)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        if actual_lp != heuristic_lp:
            failed_graphs.append(g)
    print("---- Finding Heuristic Fail Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Result: {len(failed_graphs)} graphs with wrong longest path")
    if len(failed_graphs) == 0:
        return None
    for graph in failed_graphs:
        ig.plot(graph)
    return failed_graphs

if __name__ == "__main__":
    funcs_to_test = [
        altruist_longest_path,
        prune_graph_longest_path,
        graph_stretching_longest_path,
        stretch_nodes_longest_path,
    ]
    for f in funcs_to_test:
        output = find_heuristic_fail(4, 5, f, 10)
    
