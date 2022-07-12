import igraph as ig
import random

def generate_random_graph2(n, m):

    min_edges = n-1
    max_edges = int(n*(n-1)/2)

    if m < min_edges:
        return None
    elif m > max_edges:
        return None

    g = ig.Graph(directed=False)
    g.add_vertices(n)

    all_edges = []

    for i in range(m):
        source = random.randint(0, n-1)
        target = random.randint(0, n-1)

        while source == target:
            source = random.randint(0, n-1)
            target = random.randint(0, n-1)

        pair = (source, target)
        inverted_pair = (target, source)

        while pair in all_edges or inverted_pair in all_edges:
            source = random.randint(0, n-1)
            target = random.randint(0, n-1)
            while source == target:
                source = random.randint(0, n-1)
                target = random.randint(0, n-1)
            pair = (source, target)
            inverted_pair = (target, source)

        all_edges.append(pair)

    g.add_edges(all_edges)
    return(g)