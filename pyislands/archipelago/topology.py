'''
Module contains functions for generationg islands topology.
'''

def generate_regular(num_islands, degree):
    '''
    Creates a directed, regular, fully connected graph with
    given degree of each vertex/island. This function is used
    for creating migration topology, return its adjacency list.
    '''
    idxs = list(range(num_islands))
    neighbors = [idxs[-i:] + idxs[:-i] for i in range(degree, 0, -1)]

    return list(zip(*neighbors))
