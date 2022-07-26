# Longest path heuristic benchmarking.
# Justin Xie 2022

# This code benchmarks various longest-path heuristics for
# path quality and performance.

import igraph as ig
import os
import matplotlib.pyplot as plt
from graph_to_file import read
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path
from implementing_heuristics import altruist_longest_path
from graph_pruning_most_central import prune_graph_longest_path
from stretch_total_graph import graph_stretching_longest_path
from stretch_lowest_node import stretch_nodes_longest_path
from dfs_greedy_heuristic import improved_altruist_longest_path


def print_base_stats(heuristic, n, m, runs):
    print(f"Heuristic: {heuristic.__name__}")
    print(f"Nodes: {n}")
    print(f"Edges: {m}")
    print(f"Runs: {runs}")


# Benchmarks how well a heuristic outputs 
# the exact longest path.
def complete_accuracy(n, m, heuristic):
    accurate = 0
    location = '/home/justin/work/Heuristics-Longest-Path-Project/benchmark_suite_graph_collection'
    runs = len(os.listdir(location))
    os.chdir(location)
    for file in os.listdir(location):
        g = read(file)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        print(f'Actual: {actual_lp}')
        print(f'Heuristic: {heuristic_lp}')
        if actual_lp == heuristic_lp:
            accurate += 1
    accuracy_rate = round(accurate / runs * 100, 2)
    print("---- Complete Accuracy Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Accuracy Rate: {accuracy_rate}")
    print(f"{accurate} out of {runs}")
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

    
# Plots the results of a benchmark when altering the number of vertices
# Keeping the edge to maximum possible edges ratio constant
def plot_altering_vertices(bench, funcs, starting_vertex_count, ending_vertex_count, edge_max_ratio, runs):
    x_label = input('x-axis label: ')
    y_label = input('y-axis label: ')
    title = input('Graph Title: ')
    all_y = []
   
    for i in range(len(funcs)):
        x = []
        y = []
        for number_of_vertices in range(starting_vertex_count, ending_vertex_count + 1):
            n = number_of_vertices
            m = int(n*(n-1)//2 * edge_max_ratio)
            x.append(n)
            y.append(bench(n, m, funcs[i], runs))
        all_y.append(y)

    for i in range(len(all_y)):
        plt.plot(x, all_y[i], label=funcs[i].__name__)
    plt.xlabel(x_label) 
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()


# Plots the results of a benchmark when altering
# the edges and keeping the vertex count constant
def plot_altering_edges(bench, funcs, vertex_count, runs):
    x_label = input('x-axis label: ')
    y_label = input('y-axis label: ')
    title = input('Graph Title: ')
    all_y = []
    
    for i in range(len(funcs)):
        x = []
        y = []
        starting_edge_count = vertex_count - 1
        ending_edge_count = vertex_count * (vertex_count - 1) // 2
        for number_of_vertices in range(starting_edge_count, ending_edge_count + 1):
            n = vertex_count
            m = number_of_vertices
            x.append(m)
            y.append(bench(n, m, funcs[i], runs))
        all_y.append(y)

    for i in range(len(all_y)):
        plt.plot(x, all_y[i], label=funcs[i].__name__)
    plt.xlabel(x_label) 
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    funcs_to_test = [
        prune_graph_longest_path,
        altruist_longest_path,
        graph_stretching_longest_path,
        stretch_nodes_longest_path,
        improved_altruist_longest_path
        ]
