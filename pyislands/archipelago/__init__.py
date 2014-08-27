'''
Package contains implementations of archipelago, network of islands.
Archipelago may be spread accross multiple processes, multiple computers,
but may be implemented on a single process computer.

Islands in archipelago is presented with its integer id.
'''

def form_destinations(migration_graph, airports):
    '''
    This functions forms destinations for each island emmigration
    based on adjacency matrix migration_graph. It returns tuple of tuples:

    destinations = (destinations_island_0,
                    destinations_islands_1,
                    .
                    .
                    destinations_islands_n)

    destinations_island_0 = (dst_00, dst_01, ..., dst_0m)
    destinations_island_1 = (dst_10, dst_11, ..., dst_0m)
    .
    .
    destinations_island_n = (dst_n0, dst_n1, ..., dst_0m)

    where dst_ij is an airport on island_j
    '''

    destinations = tuple(tuple(airports[idx] for idx in idxs)
                         for idxs in migration_graph)
    
    return destinations


import pyislands.archipelago.topology
import pyislands.archipelago.nonparallel
