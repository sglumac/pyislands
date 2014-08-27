'''
Synchronous Island creation for testing on a single computer,
this module connects populations/islands using simple queues/lists.
'''
from pyislands import island

import sys
if sys.version_info[0] == 3:
    from queue import Queue
else:
    from Queue import Queue
from itertools import islice
zipping = zip
if sys.version_info[0] == 2:
    from itertools import izip
    zipping = izip


def create_airports(num_islands):
    '''
    An airport is a traffic stop for an islands. An airport
    should support get, put and empty operations. Queues
    are used as an implementation of an airport.
    '''

    airports = tuple(Queue() for _ in range(num_islands))

    return airports



def get_solution(islands, num_iterations):
    '''
    Utility function used for getting a solutions from a single process algorithm.
    '''


    evolutions = map(island.evolution, islands)

    for iteration, populations in islice(enumerate(zipping(*evolutions)), num_iterations):
        best_individuals = map(min, populations)
        least_penalty, _ = min(best_individuals)
        print("iteration = {0}, penalty = {1}".
              format(iteration, least_penalty))

    penalty, solution = min(map(min, populations))

    return solution, penalty
