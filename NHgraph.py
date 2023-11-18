import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ("Coos", "Grafton"),
    ("Coos", "Carroll"),
    ("Grafton", "Carroll"),
    ("Grafton", "Belknap"),
    ("Grafton", "Merrimack"),
    ("Grafton", "Sullivan"),
    ("Carroll", "Belknap"),
    ("Carroll", "Strafford"),
    ("Belknap", "Merrimack"),
    ("Belknap", "Strafford"),
    ("Merrimack", "Strafford"),
    ("Merrimack", "Hillsborough"),
    ("Merrimack", "Sullivan"),
    ("Merrimack", "Rockingham"),
    ("Strafford", "Rockingham"),
    ("Hillsborough", "Rockingham"),
    ("Hillsborough", "Cheshire"),
    ("Hillsborough", "Sullivan"),
    ("Cheshire", "Sullivan")
]

G = nx.Graph()
G.add_edges_from(edges)

plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Graph of New Hampshire Counties")
plt.show()