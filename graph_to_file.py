import igraph as ig
import os
from treestart_gen_random_graph import basetree_random_graph

def write(graph, location, name):
    os.chdir(location)
    graph.write_lgl(name, names=None, weights=None)

def read(file):
    graph = ig.Graph.Read_Lgl(file, names=False, directed=False)
    for i in range(len(graph.vs)):
        graph.vs[i]["id"]= i
        graph.vs[i]["label"]= str(i)
    return graph

if __name__ == "__main__":
    n = int(input('n: '))
    m = int(input('m: '))
    location = '/home/justin/work/Heuristics-Longest-Path-Project/benchmark_suite_graph_collection'
    for i in range(100):
        g = basetree_random_graph(n, m)
        file_name = f'{n}_{m}graph{i}'
        write(g, location, file_name)
