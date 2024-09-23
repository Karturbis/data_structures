"""Simple script to plot Graphs from
Files in the .ajzl format"""

import matplotlib.pyplot as plt
import networkx as nx

adjacancy_list_file: str = "graph_from_adjencancy_list/adjazenzlisten_01.ajzl"

with open(adjacancy_list_file, encoding="utf-8") as reader:
    adjacancy_lines_list = reader.readlines()
nodes: list = []
edges: list = []
for line in adjacancy_lines_list:
    if line.startswith("#"):  # Make comments in the .ajzl file format possible
        continue
    line = line.split(":")
    nodes.append(line[0])
    edges_temp = line[1].split(",")
    for edge in edges_temp:
        edges.append([line[0], edge.split("(")[0], edge.split("(")[1].strip(")\n")])

print(f"Nodes: {nodes}")
print(f"Edges: {edges}")

G = nx.Graph()
G.add_nodes_from(nodes)

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=int(edge[2]))

pos = nx.spring_layout(G)
edges = G.edges(data=True)

nx.draw(G, pos, with_labels=True, node_size=1337, node_color="aquamarine")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): d["weight"] for u, v, d in edges}
)

plt.show()
