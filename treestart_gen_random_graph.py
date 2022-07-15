import igraph as ig
import random

#Below is the Pseudocode provided by Bart

# To make a "random" graph with m nodes and n edges, with m > n - 1:

#    let E be the set of all possible edges (i, j) between n vertices

#    for each vertex i from 2 to n
#        let j be a random number in the range 1..(i - 1)
#        connect i to j
#        delete (i, j) from E

#    repeat m - (n - 1) times
#        if E is empty
#            fail
#        pick a random edge (i, j) from E
#        connect i to j
#        delete (i, j) from E



#Below is the Python implementation of the above pseudocode
def basetree_random_graph(n, m):
    
    #Checking if the number of edges is below the minimum
    if m < n-1:
        return None

    #Creating intial vertices of the graph
    g = ig.Graph(directed=False)

    g.add_vertices(n)

    for i in range(len(g.vs)):
        g.vs[i]["id"]= i
        g.vs[i]["label"]= str(i)
    
    #Finding all possible source-target vertex pairs by looping through all vertices and pairing them with all vertices larger than it
    #Avoids redudant pairs
    possible_edge_set = set()
    for i in range(n):
        for j in range(i+1, n):
            possible_edge_set.add((i, j))

    #Skips vertex 0, starting at vertex 1 and loops through each vertex and randomly selects a target vertex
    #The number of the source vertex is larger than the target vertex
    for i in range(1, n):
        j = random.randint(0, i-1)
        edge_pair = (j, i) #Flips the vertex order to fit the format of the tuples in the possible_edge_set
        g.add_edge(i,j)
        possible_edge_set.remove(edge_pair)       

    #For the remaining edges, if any, the source-target pairs are randomly selected from the possible set and added
    for k in range(m-(n-1)):
        if not possible_edge_set:
            return None #If this if statement is entered it means that the edges inputted into the function was greater than what is possible
        edge_pair = random.choice(tuple(possible_edge_set))
        possible_edge_set.remove(edge_pair)
        i = edge_pair[0]
        j = edge_pair[1]
        g.add_edge(i,j)
    
    return g