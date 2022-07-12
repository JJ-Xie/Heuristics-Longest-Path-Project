import time
from translated_pseudo_random_graph_gen import random_graph


for i in range(50):
    vertices = int(input("Vertices: "))
    edges = int(vertices*(vertices-1)/2)

    start_time = time.time()
    output = random_graph(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Runtime: {runtime} seconds ---')