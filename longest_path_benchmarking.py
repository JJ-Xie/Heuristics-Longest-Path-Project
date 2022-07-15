#Benchmarks for various longest path algorithms and heuristics
#Justin Xie 2022

import igraph as ig
import time

from treestart_gen_random_graph import basetree_random_graph
from find_longest_path import find_longest_path
from implementing_heuristics import altruist_longest_path


#Testing brute force runtimes as a function of n nodes and a constant edge ratio
def nodes_brute_benchmark(end_node_count):
    print(f'---- Runtime as a function of n | Testing brute force algorithm ----')
    for i in range(3, end_node_count):
        total_runtime = 0
        n = i
        m = i*(i-1)//3
        
        for j in range(50):
            g = basetree_random_graph(n,m)

            start_time = time.time()
            longest_path_length = find_longest_path(g)
            runtime = time.time() - start_time
            total_runtime += runtime
        
        average_runtime = total_runtime/50
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')


#Testing heuristic runtimes as a function of n nodes and a constant edge ratio
def nodes_antigreedy_benchmark(end_node_count):
    print(f'---- Runtime as a function of n | Testing antigreedy heuristic ----')
    for i in range(3, end_node_count):
        total_runtime = 0
        n = i
        m = i*(i-1)//3
        
        for j in range(50):
            g = basetree_random_graph(n,m)

            start_time = time.time()
            longest_path_length = altruist_longest_path(g)
            runtime = time.time() - start_time
            total_runtime += runtime
        
        average_runtime = total_runtime/50
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')


#Testing brute force runtimes as a function of m edges and a constant node count
def edges_brute_benchmark(number_of_nodes):
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
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')


#Testing brute force runtimes as a function of m edges and a constant node count
def edges_antigreedy_benchmark(number_of_nodes):
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
        print(f'Number of Nodes: {n}, Number of Edges: {m}, Runtime: {average_runtime}')

