# Heuristics-Longest-Path-Project
Justin Xie 2022

## About the Project
This project aims to use heuristics in the longest simple path problem. This repository contains the heuristics, graphs, and benchmarking suite for executing the heuristics.

## About the Repository
Ths repository contains the heuristics, random graph generators, graphs sets, and benchmark suite used during research into the longest path problem. The heuristics directory contains all heuristics explored and an init file that modulates the heuristics for organization and benchmark purposes. The random graph generator in the file treestart_gen_random_graph.py generated the graph sets in the directory benchmark_graph_sets for use in the benchmark suite.

- **benchmark_graph_sets:** An array of random graph sets generated for consistent benchmarking results among heuristics.
- **heuristics:** Collection of heuristics explored in this project.
- **benchmark_suite.py:** Contains benchmark functions for accuracy, error, and runtime that can be run as functions of the number of vertices or edges.
- **find_longest_path.py:** Finds longes path through brute-force method of finding all simple paths.
- **graph_to_file.py:** Converts Python-igraph graphs into lgl files for storage and from lgl files back to igraph graphs.
- **treestart_gen_random_graph.py:** Generates random graph by starting with a random, connected tree and adding random edges.
- **visualizing_graph_periphery.py:** Colors a random graph's vertices in a gradient based on the total vertex periphery.

## Prerequisites for Execution
1. The code in the repository was created using Python 3.10.4. Installation can be done through the command line:

```bash
sudo apt-get update
sudo apt-get install python3.10
```

2. The heuristics, graphs, and benchmark suite require the [Python-igraph](https://igraph.org/python/) and the [Matplotlib](https://matplotlib.org/) packages to run. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install igraph and Matplotlib. Use pip3 for Python3.

```bash
pip3 install igraph
pip3 install matplotlib
```

## Usage
All testing of the heuristics can be done through the benchmark suite file. It contains 3 benchmark functions, 2 benchmark execution functions, and function to find graphs that cause heuristics to return incorrect answers.

#### Benchmark Functions:
Each function is given a specific vertex (n) and edge count (m), a heuristic, and a location and a location to the save graph files.

1. **Accuracy:** Returns the percentage of graphs where the given heuristic returned the correct answer. 

2. **Error:** Returns the average difference between the the longest path returned by the heuristic and the correct longest path over all inputted graphs.

3. **Runtime:** Returns the average runtime of the given heuristic over all inputted graphs.

#### Benchmark Execution Functions:
1. **execute_specific_benchmark_set:** Given a specific vertex (n) and edge (m) count, heuristic, and benchmark function. This execution function will run the benchmark on the heuristic on graph sets with n vertices and m edges.

2. **plot_altering_edges:** Given a specific vertex count, a single or group of heuristics, and a benchmark function. This execution function loop through all possible edge counts for the given vertex count and execute the benchmark for all given heuristics for the graph sets at each vertex and edge combination.

#### find_heuristic_fail 
Given a vertex and edge count, a heuristic, and a number of runs to loop through. The function generates random graphs with n vertices an m edges and returns the number of graphs where the heuristic failed to yield the correct answer. It then graphs them if inputted 'y' at your discretion.

### Using the Benchmark Execution Functions
In the main function of the benchmark suite, you can call any of the benchmark execution functions. For example, to plot the accuracy of all heuristics on graphs with 8 vertices and a changing number of edges, you could call this function in the main function:

```python
if __name__ == "__main__":
    plot_altering_edges(8, heuristics.all, accuracy)
```

Disclaimer: If the number of vertices and edges inputted are too large, the benchmarking functions may not work or could crash due to the exponential properties of the find_longest_path function that checks answers.

## License
This work is made available under the "GNU General Public License v3.0". Please see the file LICENSE in this distribution for license terms.

## Acknowledgements
Thank you to Bart Massey and Cassaundra Smith for helping me in this exploration of the Heuristics in the Longest Simple Path Problem.