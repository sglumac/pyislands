from pyislands import evolution as ev

import multiprocessing
from itertools import islice
import functools as fcn


def create_airports(num_islands):
    '''
    An airport is a traffic stop for an islands. An airport
    should support get, put and empty operations. Queues
    are used as an implementation of an airport.
    '''

    manager = multiprocessing.Manager()
    airports = tuple(manager.Queue() for _ in range(num_islands))

    return airports


def __get_solution(num_iterations, island):
    for population in islice(ev.evolution(island), num_iterations):
        print min(population).penalty
    return min(population)


def get_solution(islands, num_iterations):
    '''
    Utility function used for getting a solutions from a single process algorithm.
    '''

    num_islands = len(islands)
    pool = multiprocessing.Pool(processes=num_islands)

    solutions = pool.map(fcn.partial(__get_solution, num_iterations), islands)

    return min(solutions)
