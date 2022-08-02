# Heuristics-Longest-Path-Project
Justin Xie 2022

## About the Project
This project aims to use heuristics in the longest simple path problem. This repository contains the heuristics, graphs, and benchmarking suite for executing the heuristics.

## About the Repository
Ths repository contains the heuristics, random graph generators, graphs sets, and benchmark suite used during research into the longest path problem. The heuristics directory contains all 6 heuristics explored and an init file that modulates the heuristics for organization and benchmark purposes. The random graph generator in the file treestart_gen_random_graph.py generated the graph sets in the directory benchmark_graph_sets

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


## License
This work is made available under the "GNU General Public License v3.0". Please see the file LICENSE in this distribution for license terms.

## Acknowledgements