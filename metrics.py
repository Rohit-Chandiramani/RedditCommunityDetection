import networkx as nx
import numpy as np

def calculate_coverage(G, partitions):
    intra_edges = sum([1 for u, v in G.edges if partitions[u] == partitions[v]])
    total_edges = G.number_of_edges()
    return intra_edges / total_edges

def calculate_density(G, partition):
    densities = []
    for community in set(partition.values()):
        nodes = [node for node in G.nodes if partition[node] == community]
        subgraph = G.subgraph(nodes)
        if len(nodes) > 1:
            densities.append(nx.density(subgraph))
    return np.mean(densities)

def calculate_clustering_coefficient(G, partition):
    clustering_coeffs = []
    for community in set(partition.values()):
        nodes = [node for node in G.nodes if partition[node] == community]
        subgraph = G.subgraph(nodes)
        clustering_coeffs.append(nx.average_clustering(subgraph))
    return np.mean(clustering_coeffs)

def calculate_conductance(G, partition):
    conductances = []
    for community in set(partition.values()):
        nodes = [node for node in G.nodes if partition[node] == community]
        subgraph = G.subgraph(nodes)
        if len(nodes) > 0:
            cut_size = nx.cut_size(G, nodes)
            volume = nx.volume(G, nodes)
            conductances.append(cut_size / volume if volume > 0 else 0)
    return np.mean(conductances)
