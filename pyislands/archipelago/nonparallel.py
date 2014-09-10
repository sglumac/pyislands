'''
Synchronous Island creation for testing on a single computer,
this module connects populations/islands using simple queues/lists.
'''
from pyislands.evolution import finite_evolution

import sys
if sys.version_info[0] == 2:
    import Queue as queue
    from itertools import izip as zip
else:
    import queue
from itertools import islice


def create_airports(num_islands):
    '''
    An airport is a traffic stop for an islands. An airport
    should support get, put and empty operations. Queues
    are used as an implementation of an airport.
    '''

    airports = tuple(queue.Queue() for _ in range(num_islands))

    return airports



def get_solution(islands, num_iterations, verbose=True):
    '''
    Utility function used for getting a solutions from a single process algorithm.
    '''


    evolutions = (finite_evolution(num_iterations, island)
                  for island in islands)

    for iteration, populations in enumerate(zip(*evolutions)):
        if verbose:
            best_individuals = map(min, populations)
            least_penalty, _ = min(best_individuals)
            print("iteration = {0}, penalty = {1}".
                  format(iteration, least_penalty))

    return min(map(min, populations))
