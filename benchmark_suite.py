
import igraph as ig
import matplotlib.pyplot as plt
from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path
from implementing_heuristics import altruist_longest_path
from graph_pruning_most_central import prune, prune_graph_longest_path
from stretch_total_graph import graph_stretching_longest_path
from stretch_lowest_node import stretch_nodes_longest_path


#Benchmarks how well a heuristic outputs the exact longest path
def complete_accuracy(n, m, func, runs):
    accurate = 0
    for run in range(runs):
        g = basetree_random_graph(n, m)
        actual_lp = find_longest_path(g)
        heuristic_lp = func(g)
        if actual_lp == heuristic_lp:
            accurate += 1
    accuracy_rate = round(accurate/runs * 100, 2)
    print(f'''---- Complete Accuracy Benchmark ----\nFunction: {func.__name__}\nNodes: {n}\nEdges: {m}\nRuns: {runs}\nAccuracy Rate: {accuracy_rate}\n''')
    return accuracy_rate


#Benchmarks how far off a function is from the actual longest path
def error_accuracy(n, m, func, runs):
    total_difference = 0
    for run in range(runs):
        g = basetree_random_graph(n, m)
        actual_lp = find_longest_path(g)
        heuristic_lp = func(g)
        accuracy_diffference = actual_lp - heuristic_lp
        total_difference += accuracy_diffference
    average_difference = round(total_difference/runs, 2)
    print(f'''---- Error Accuracy Benchmark ----\nFunction: {func.__name__}\nNodes: {n}\nEdges: {m}\nRuns: {runs}\n Average Error: {average_difference}\n''')
    return average_difference


#Finds the number of and plots the graphs that cause the heuristic to fail to find the correct longest path
def find_heuristic_fail(n, m, func, runs):
    failed_graphs = []
    for run in range(runs):
        g = basetree_random_graph(n, m)
        actual_lp = find_longest_path(g)
        heuristic_lp = func(g)
        if actual_lp != heuristic_lp:
            failed_graphs.append(g)
    if len(failed_graphs) == 0:
        print(f'''---- Finding Heuristic Fail Benchmark ----\nFunction: {func.__name__}\nNodes: {n}\nEdges: {m}\nRuns: {runs}\nResult: No graphs resulted in wrong longest path\n''')
        return None
    else:
        print((f'''---- Finding Heuristic Fail Benchmark ----\nFunction: {func.__name__}\nNodes: {n}\nEdges: {m}\nRuns: {runs}\nResult: {len(failed_graphs)}graphs resulted in wrong longest path\n'''))
        for graph in failed_graphs:
            ig.plot(graph)
        return failed_graphs


#Plots the results of a benchmark when altering the number of vertices
def plot_perf_alt_n(bench, func, starting_vertex_count, ending_vertex_count, edge_max_ratio, runs):
    x = []
    y = []
    x_label = input('x-axis label: ')
    y_label = input('y-axis label: ')
    title = input('Graph Title: ')
    for number_of_vertices in range(starting_vertex_count, ending_vertex_count + 1):
        n = number_of_vertices
        m = int(n*(n-1)//2 * edge_max_ratio)
        x.append(n)
        y.append(bench(n, m, func, runs))
    plt.scatter(x, y)
    plt.xlabel(x_label) 
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def plot_perf_alt_m(bench, func, vertex_count, runs):
    x = []
    y = []
    x_label = input('x-axis label: ')
    y_label = input('y-axis label: ')
    title = input('Graph Title: ')
    starting_edge_count = vertex_count - 1
    ending_edge_count = vertex_count * (vertex_count - 1) // 2
    for number_of_vertices in range(starting_edge_count, ending_edge_count + 1):
        n = vertex_count
        m = number_of_vertices
        x.append(m)
        y.append(bench(n, m, func, runs))
    plt.scatter(x, y)
    plt.xlabel(x_label) 
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()



if __name__ == "__main__":
    funcs_to_test = [prune_graph_longest_path]
    for f in funcs_to_test:
        plot_perf_alt_m(complete_accuracy, f, 7, 10000)
    