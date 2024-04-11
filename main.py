import networkx as nx
import matplotlib.pyplot as plt

# Load the Caltech network
G_caltech = nx.read_gml('path_to_caltech.gml')

# Print basic information to verify it's loaded correctly
print(nx.info(G_caltech))
