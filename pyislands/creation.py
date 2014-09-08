from pyislands.types import create_individual

import functools as fcn


def __create_population(generate, evaluate, population_size):
    genotypes = tuple(generate() for _ in range(population_size))
    population = tuple(map(fcn.partial(create_individual, evaluate), genotypes))

    return population


def get_create_population(generate, evaluate, population_size):
    '''
    This function is used in evolution to create an initial
    population.
    '''

    return fcn.partial(__create_population, generate, evaluate, population_size)
