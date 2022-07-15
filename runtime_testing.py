import time
from translated_pseudo_random_graph_gen import random_graph
from generate_random_graph_v1 import generate_random_graph1
from generate_random_graph_v2 import generate_random_graph2

#Setting runtime intervals(Number of vertices in graph)
testing_intervals = [50, 100, 150, 200, 250, 300, 350, 400]

#Testing translated online psuedo runtime
for interval in testing_intervals:
    vertices = interval
    edges = int(vertices*(vertices-1)/2)

    start_time = time.time()
    output = random_graph(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Translated Pseudo Runtime: {runtime} seconds --- Number of Nodes: {interval} ---')

#Testing my random graph generation v1 runtime
for interval in testing_intervals:
    vertices = interval
    edges = int(vertices*(vertices-1)/2)

    start_time = time.time()
    output = generate_random_graph1(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Generate_Random_Version1 Runtime: {runtime} seconds --- Number of Nodes: {interval} ---')

#Testing my random graph generation v2 runtime
for interval in testing_intervals:
    vertices = interval
    edges = int(vertices*(vertices-1)/2)

    start_time = time.time()
    output = generate_random_graph2(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Generate_Random_Version1 Runtime: {runtime} seconds --- Number of Nodes: {interval} ---')