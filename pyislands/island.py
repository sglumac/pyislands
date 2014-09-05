from pyislands.types import create_individual, Individual

import os
import functools as fcn
from itertools import islice, count, takewhile


def create_population(generate, evaluate, population_size):
    '''
    This function is used in steady_evolve to create an initial
    population.
    '''
    genotypes = tuple(generate() for _ in range(population_size))
    population = tuple(map(fcn.partial(create_individual, evaluate), genotypes))

    return population


def evolution(island):
    '''
    Infinite generator for evolution of some population.
    This generator yields population:
        population - tuple together containing tuples/individuals

    population_0 = create()
    population_1 = evolve(population_0, info_0)
    .
    .
    population_k = evolve(population_k-1, info_k-1)
    .
    .

    Since population is a tuple/an immutable type, a population cannot be
    influenced by outside functions. Population can be used only to gather
    statistics

    If no immigration and emmigration is used this island evolution 
    becomes a classical genetic algorithm.
    '''

    population = island.create_population()

    for iteration in count():
        yield population

# Immigration - Outside individuals are inhabiting an island
        if island.immigrate:
            population = island.immigrate(population)

# Evolution - Each island population is evolved into the next generation
        population = island.evolve(population)

# Emmigration - Sends individuals (clones) from one population onto voyage
        if island.emmigrate and iteration % island.migration_interval == 0:
            island.emmigrate(population)


def get_solution(island, num_iterations):
    '''
    Utility function used for getting a solution from a single islands.
    '''

    for iteration, population in islice(enumerate(evolution(island)), num_iterations):
        least_penalty, _ = min(population)
        pid = os.getpid()
        print("pid = {0}, iteration = {1}, penalty = {2}".
              format(pid, iteration, least_penalty))

    return min(population)


def get_stagnation_solution(island, max_stagnation):

    stagnation = 0
    best = Individual(float('inf'), None)
    iteration = 0

    for population in takewhile(lambda dummy: stagnation < max_stagnation,
                                evolution(island)):

        population_best = min(population)

        if population_best < best:
            stagnation = 0
            best = min(population)


        stagnation += 1
        iteration += 1
        print stagnation, iteration, best.penalty

    return min(population), iteration
