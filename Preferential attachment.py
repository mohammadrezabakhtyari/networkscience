import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from operator import itemgetter
from collections import Counter


n = 1000  # number of nodes
gama = 0.5
start_nodes = [1, 2, 3, 4]
start_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
DG = nx.DiGraph()
DG.add_nodes_from(start_nodes)
DG.add_edges_from(start_edges)
# add n nodes to graph by preferential attachment
for i in range(len(start_nodes)+1, n+1):
    randomize = np.random.random()
    # a link is to a page chosen uniformly at random
    if randomize < gama:
        random_node = random.choice(np.array(DG.nodes()))
        DG.add_node(i)
        DG.add_edge(i, random_node)
    # link is copied from existing links
    else:
        random_edge = random.choice(np.array(DG.edges()))
        DG.add_node(i)
        DG.add_edge(i, random_edge[1])


# plotting log-log
degrees = DG.degree()
sorted_degrees = sorted(degrees, key=itemgetter(1))
numer_of_degrees = Counter(elem[1] for elem in sorted_degrees)
hist = []
for i in numer_of_degrees:
    hist.append(numer_of_degrees[i]/float(nx.number_of_nodes(DG)))
degree_values = [v for v in numer_of_degrees]
plt.plot(degree_values, hist, 'o')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.xscale('log')
plt.yscale('log')
plt.show()


# plottin complimentary cumulative degree distribution
k = np.array(degree_values).max()
comp_cum_deg = []

for i in range(1, k+1):
    count = 0
    for j in numer_of_degrees:
        if j >= i:
            count += numer_of_degrees[j]
    comp_cum_deg.append(count)

k_list = np.arange(1, k+1)
plt.plot(k_list, comp_cum_deg, 'o')
plt.xlabel('k')
plt.ylabel('Fraction of Nodes')
plt.xscale('log')
plt.yscale('log')
plt.show()