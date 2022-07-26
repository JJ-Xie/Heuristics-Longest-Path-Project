import igraph as ig
import os
from treestart_gen_random_graph import basetree_random_graph

#Writes graph into lgl file at given location
def write(graph, name):
    graph.write_lgl(name, names=None, weights=None)

#Reads graph from lgl file
def read(file):
    graph = ig.Graph.Read_Lgl(file, names=False, directed=False)
    for i in range(len(graph.vs)):
        graph.vs[i]["id"]= i
        graph.vs[i]["label"]= str(i)
    return graph

if __name__ == "__main__":
    n = input('N: ')
    m = input('M: ')

    if n < 10:
        str_n = f'0{n}'
    else:
        str_n = str(n)
    if m < 10:
        str_m = f'0{m}'
    else:
        str_m = str(m)

    directory = os.environ.get('PWD')
    os.chdir(f'{directory}/benchmark_graph_sets')
    os.mkdir(f'{str_n}_{str_m}')
    bench_set = f'{directory}/benchmark_graph_sets/{str_n}_{str_m}'
    os.chdir(bench_set)
    for i in range(100):
        g = basetree_random_graph(n, m)
        file_name = f'{str_n}_{str_m}_graph_{i}'
        write(g, file_name)
