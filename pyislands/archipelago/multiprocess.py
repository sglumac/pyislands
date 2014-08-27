from pyislands import island

import multiprocessing
from itertools import repeat
from operator import methodcaller


def create_airports(num_islands):
    '''
    An airport is a traffic stop for an islands. An airport
    should support get, put and empty operations. Queues
    are used as an implementation of an airport.
    '''

    manager = multiprocessing.Manager()
    airports = tuple(manager.Queue() for _ in range(num_islands))

    return airports


def get_solution(islands, num_iterations):
    '''
    Utility function used for getting a solutions from a single process algorithm.
    '''

    num_islands = len(islands)
    pool = multiprocessing.Pool(processes=num_islands)

    futures = [pool.apply_async(island.get_solution, (isl, num_iterations))
               for isl in islands]

    solutions = tuple(map(methodcaller('get'), futures))

    return min(solutions)
