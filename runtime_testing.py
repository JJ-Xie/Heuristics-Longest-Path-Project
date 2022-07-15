import time
from treestart_gen_random_graph import basetree_random_graph
from unconnected_random_graph import unconnected_random_graph

#Setting runtime intervals(Number of vertices in graph)
testing_intervals = [50, 100, 150, 200, 250, 300, 350, 400]

#Testing treestart random graph runtime
for interval in testing_intervals:
    vertices = interval
    edges = int(vertices*(vertices-1)/2)

    start_time = time.time()
    output = basetree_random_graph(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Translated Pseudo Runtime: {runtime} seconds --- Number of Nodes: {interval} ---')

#Testing my random unconnected graph runtime
for interval in testing_intervals:
    vertices = interval
    edges = int(vertices*(vertices-1)/2)

    start_time = time.time()
    output = unconnected_random_graph(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Generate_Random_Version1 Runtime: {runtime} seconds --- Number of Nodes: {interval} ---')