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
    n = int(input('Number of Vertices: '))
    upper_bound = int(input("Upper Bound Edge Count: "))
    for j in range(n-1, upper_bound+1):
        m = j
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
        for i in range(1, 101):
            if i < 10:
                str_i = f'0{i}'
            else:
                str_i = str(i)
            g = basetree_random_graph(n, m)
            file_name = f'{str_n}_{str_m}_graph_{str_i}'
            write(g, file_name)
