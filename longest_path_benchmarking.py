#Benchmarks for various longest path algorithms and heuristics
#Justin Xie 2022

import igraph as ig
import time
import matplotlib.pyplot as plt
import numpy as np

from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path
from implementing_heuristics import altruist_longest_path


#Testing brute force runtimes as a function of n nodes and a constant edge ratio of 3/4
def nodes_brute_benchmark(end_node_count):
    x = np.array([])
    y = np.array([])
    print(f'---- Runtime as a function of n | Testing brute force algorithm ----')
    for i in range(3, end_node_count):
        total_runtime = 0
        n = i
        m = 3*i*(i-1)//8
        
        for j in range(50):
            g = basetree_random_graph(n,m)

            start_time = time.time()
            longest_path_length = find_longest_path(g)
            runtime = time.time() - start_time
            total_runtime += runtime
        
        average_runtime = total_runtime/50
        x = np.append(x, n)
        y = np.append(y, average_runtime)
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')
    
    plt.scatter(x, y)
    plt.xlabel('Number of Nodes') 
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime of Brute-Force algorithm with increasing nodes')
    plt.show()


#Testing heuristic runtimes as a function of n nodes and a constant edge ratio of 3/4
def nodes_antigreedy_benchmark(end_node_count):
    x = np.array([])
    y = np.array([])
    print(f'---- Runtime as a function of n | Testing antigreedy heuristic ----')
    for i in range(3, end_node_count):
        total_runtime = 0
        n = i
        m = 3*i*(i-1)//8
        
        for j in range(50):
            g = basetree_random_graph(n,m)

            start_time = time.time()
            longest_path_length = altruist_longest_path(g)
            runtime = time.time() - start_time
            total_runtime += runtime
        
        average_runtime = total_runtime/50
        x = np.append(x, n)
        y = np.append(y, average_runtime)
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')

    plt.scatter(x, y)
    plt.xlabel('Number of Nodes') 
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime of Heuristic with increasing nodes')
    plt.show()

#Testing brute force runtimes as a function of m edges and a constant node count
def edges_brute_benchmark(number_of_nodes):
    x = np.array([])
    y = np.array([])
    n = number_of_nodes
    m_lb = n - 1
    m_ub = n*(n-1)//2
    print(f'---- Runtime as a function of m | Testing brute force algorithm ----')
    for m in range(m_lb, m_ub + 1):
        total_runtime = 0
        
        for j in range(50):
            g = basetree_random_graph(n,m)

            start_time = time.time()
            longest_path_length = find_longest_path(g)
            runtime = time.time() - start_time
            total_runtime += runtime
        
        average_runtime = total_runtime/50
        x = np.append(x, m)
        y = np.append(y, average_runtime)
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')

    plt.scatter(x, y)
    plt.xlabel('Number of Edges') 
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime of Brute-Force algorithm with increasing edges')
    plt.show()


#Testing brute force runtimes as a function of m edges and a constant node count
def edges_antigreedy_benchmark(number_of_nodes):
    x = np.array([])
    y = np.array([])
    n = number_of_nodes
    m_lb = n - 1
    m_ub = n*(n-1)//2
    print(f'---- Runtime as a function of m | Testing antigreedy heuristic ----')
    for m in range(m_lb, m_ub + 1):
        total_runtime = 0
        
        for j in range(50):
            g = basetree_random_graph(n,m)

            start_time = time.time()
            longest_path_length = altruist_longest_path(g)
            runtime = time.time() - start_time
            total_runtime += runtime
        
        average_runtime = total_runtime/50
        x = np.append(x, m)
        y = np.append(y, average_runtime)
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')
    
    plt.scatter(x, y)
    plt.xlabel('Number of Edges') 
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime of Heuristic with increasing edges')
    plt.show()
