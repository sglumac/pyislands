'''
Synchronous Island creation for testing on a single computer,
this module connects populations/islands using simple queues/lists.
'''
import sys
if sys.version_info[0] == 3:
    from queue import Queue
else: 
    from Queue import Queue
from operator import itemgetter


def create_airports(num_islands):
    '''
    An airport is a traffic stop for an islands. An airport
    should support get, put and empty operations. Queues
    are used as an implementation of an airport.
    '''

    airports = tuple(Queue() for _ in range(num_islands))

    return airports


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


def evolution(islands):
    '''
    This is a Python generate which yields tuple of populations inhabiting
    abstract islands.
    '''
    evolves, immigrations, emmigrations = zip(*islands)

# Since this is a single process implementation, populations are stored
# list, not on the separate islands (processes)
    populations = tuple(evolve() for evolve in evolves)

    while True:
        yield populations

# Immigration - Outside individuals are inhabiting an island
        populations = (immigrate(population) for immigrate, population
                       in zip(immigrations, populations))

# Evolution - Each island population is evolved into the next generation
        populations = tuple(evolve(population) for evolve, population
                            in zip(evolves, populations))

# Emmigration - Sends individuals (clones) from one population onto voyage
        for emmigrate, population in zip(emmigrations, populations):
            emmigrate(population)
