import igraph as ig
import time
import numpy as np
import random
import matplotlib.pyplot as plt

def random_graph(n, m):
    if m < n-1:
        return None

    g = ig.Graph(directed=False)
    g.add_vertices(n)
    
    possible_edge_set = set()
    for i in range(n):
        for j in range(i+1, n):
            possible_edge_set.add((i, j))

    for i in range(1, n):
        j = random.randint(0, i-1)
        edge_pair = (j, i)
        g.add_edge(i,j)
        possible_edge_set.remove(edge_pair)       

    for k in range(m-(n-1)):
        if not possible_edge_set:
            return None
        edge_pair = random.choice(tuple(possible_edge_set))
        possible_edge_set.remove(edge_pair)
        i = edge_pair[0]
        j = edge_pair[1]
        g.add_edge(i,j)
    
    return g

for i in range(50):
    vertices = int(input("Vertices: "))
    edges = int(3*vertices*(vertices-1)/8)

    start_time = time.time()
    output = random_graph(vertices, edges)
    runtime = time.time() - start_time
    print(f'--- Runtime: {runtime} seconds ---')

'''
x = np.array([])
y = np.array([])


vertex_list = [10, 20, 30, 40, 50, 100, 150, 200, 250]

for loops in range(len(vertex_list)):
    print(f'Running Edges Number: {vertex_list[loops]}')
    runtime_list = []
    for i in range(25):
        vertices = vertex_list[loops]
        edges = int(3*vertices*(vertices-1)/8)
        start_time = time.time()
        output = random_graph(vertices, edges)
        runtime = time.time() - start_time
        runtime_list.append(runtime)

    avg_runtime = sum(runtime_list)/len(runtime_list)
    x = np.append(x, loops)
    y = np.append(y, avg_runtime)
    
plt.scatter(x, y)
plt.show()
'''