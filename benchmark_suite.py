# Longest path heuristic benchmarking.
# Justin Xie 2022

# This code benchmarks various longest-path heuristics for
# path quality and performance.

import igraph as ig
import os
import matplotlib.pyplot as plt
import copy
import time
import heuristics
from graph_to_file import read
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path


# Prints basic stats for each run
def print_base_stats(heuristic, n, m, runs):
    print(f"Heuristic: {heuristic.__name__}")
    print(f"Nodes: {n}")
    print(f"Edges: {m}")
    print(f"Runs: {runs}")
    

# Alters n and m values for matching with file names
def formatting(n, m):
    if n < 10:
        str_n = f'0{n}'
    else:
        str_n = str(n)
    if m < 10:
        str_m = f'0{m}'
    else:
        str_m = str(m)
    
    return str_n, str_m


# Benchmarks how well a heuristic outputs 
# the exact longest path.
# Given a certain number of vertices, 
# edges, and where the benchmark graph set is located
def accuracy(n, m, heuristic, location):
    accurate = 0
    os.chdir(location)
    runs = len(os.listdir())
    for file in sorted(os.listdir()):
        g = read(file)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        if actual_lp == heuristic_lp:
            accurate += 1
    accuracy_rate = round(accurate / runs * 100, 2)
    print("---- Complete Accuracy Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Accuracy Rate: {accuracy_rate}")
    print(f"{accurate} out of {runs}")
    return accuracy_rate


# Benchmarks how far off a function is from the actual longest path.
# Given a certain number of vertices, edges
# and where the benchmark graph set is located
def error(n, m, heuristic, location):
    total_difference = 0
    os.chdir(location)
    runs = len(os.listdir())
    for file in sorted(os.listdir()):
        g = read(file)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        accuracy_diffference = actual_lp - heuristic_lp
        total_difference += accuracy_diffference
    average_difference = round(total_difference / runs, 2)
    print("---- Error Accuracy Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Average Error: {average_difference}")
    return average_difference


# Benchmarks runtime of heuristics
def runtime(n, m, heuristic, location):
    total_runtime = 0
    os.chdir(location)
    runs = len(os.listdir())
    for file in sorted(os.listdir()):
        g = read(file)
        start_time = time.time()
        heuristic(g)
        runtime = time.time() - start_time
        total_runtime += runtime
    average_runtime = total_runtime / runs
    print("---- Runtime Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f'Average Runtime: {average_runtime}')
    return average_runtime


# Benchmarks specific graph set on single heuristic
def execute_specific_benchmark_set(n, m, heuristics, benchmark):
    for heuristic in heuristics:
        directory = os.environ.get('PWD')
        bench_set = f'{directory}/benchmark_graph_sets/'
        os.chdir(bench_set)
        str_n, str_m = formatting(n, m)
        location = f'{bench_set}{str_n}_{str_m}'
        benchmark(n, m, heuristic, location)


# Benchmarks all graph sets on given heuristics
def execute_all_benchmark_sets(heuristics, benchmark): 
    directory = os.environ.get('PWD')
    bench_set = f'{directory}/benchmark_graph_sets/'
    os.chdir(bench_set)
    for heuristic in heuristics:
        dir_list = sorted(os.listdir())
        print(dir_list)
        for dir in dir_list:
            dir_name_split = dir.split('_')
            location = f'{bench_set}/{dir}'
            benchmark(dir_name_split[0], dir_name_split[1], heuristic, location)


# Plots the results of a benchmark when altering
# the number of edges and keeping the vertices the same
# Runs all graph sets with the same given vertex count 
def plot_altering_edges(vertices, heuristics, benchmark):
    x_label = input('x-axis label: ')
    y_label = input('y-axis label: ')
    title = input('Graph Title: ')
    all_y = []
    last_x = []
    for i in range(len(heuristics)):
        directory = os.environ.get('PWD')
        bench_set = f'{directory}/benchmark_graph_sets/'
        os.chdir(bench_set)
        x = []
        y = []
        dir_list = sorted(os.listdir())
        for dir in dir_list:
            dir_name_split = dir.split('_')
            if int(dir_name_split[0]) == vertices:
                n = vertices
                m = int(dir_name_split[1])
                location = f'{bench_set}{dir}'
                x.append(m)
                y.append(benchmark(n, m, heuristics[i], location))
        if y:
            all_y.append(y)
        if x:
            last_x = x

    for i in range(len(all_y)):
        plt.plot(last_x, all_y[i], label=heuristics[i].__name__)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()


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


# Finds the number of and plots the graphs that cause the
# heuristic to fail to find the correct longest path
def find_heuristic_fail(n, m, heuristic, runs):
    failed_graphs = []
    for run in range(runs):
        g = basetree_random_graph(n, m)
        original_g = copy.deepcopy(g)
        actual_lp = find_longest_path(g)
        heuristic_lp = heuristic(g)
        if actual_lp != heuristic_lp:
            failed_graphs.append(original_g)
    print("---- Finding Heuristic Fail Benchmark ----")
    print_base_stats(heuristic, n, m, runs)
    print(f"Result: {len(failed_graphs)} graphs with wrong longest path")
    if len(failed_graphs) == 0:
        return None
    for graph in failed_graphs:
        ig.plot(graph)
        print(find_longest_path(graph))
        print(heuristic(graph))
        to_continue = input('Continue Showing Graphs? ')
        if to_continue != 'y':
            break


if __name__ == "__main__":
    plot_altering_edges(10, heuristics.all, runtime)
