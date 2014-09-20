from pyislands.evolution import finite_evolution

import multiprocessing
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


def __get_solution(num_iterations, island, verbose=False):
    for population in finite_evolution(num_iterations, island):
        if verbose:
            best = min(population)
            print("penalty = {0}".format(best.penalty))
    return min(population)


def get_solution(islands, num_iterations, verbose):
    '''
    Utility function used for getting a solutions from a single process algorithm.
    '''

    num_islands = len(islands)
    pool = multiprocessing.Pool(processes=num_islands)

    solution_after_niter = fcn.partial(__get_solution, num_iterations,
                                       verbose=verbose) 

    solutions = pool.map(solution_after_niter, islands)

    return min(solutions)
