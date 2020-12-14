import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import collections

header_list = ["a", "b", "w"]
E = pd.read_csv('data/insecta-ant-colony4-day22.edges', sep=" ",
                header=None, names=header_list)
G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
nx.draw(G)

degrees = G.degree()

avg = sum([d for (n, d) in nx.degree(G)]) / float(G.number_of_nodes())
density = (2*float(G.number_of_edges())) / \
    (float(G.number_of_nodes())*float(G.number_of_nodes()-1))
diameter = nx.diameter(G, e=None, usebounds=False)
clustering = nx.average_clustering(G)

# The degree distribution P(k) of a network
degree_sequence = sorted([d for n, d in G.degree()],
                         reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

print("Diameter is ", diameter)
print("Number of Nodes", nx.number_of_nodes(G))
print("Number of Edges", nx.number_of_edges(G))
print("Number of average Degree", avg)
print("Density is ", density)
print("The Clustering Coefficient of the graph is ", clustering)

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="b")

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

plt.show()
