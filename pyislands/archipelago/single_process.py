'''
Synchronous Island creation for testing on a single computer,
this module connects populations/islands using simple queues/lists.
'''
import random
from operator import itemgetter, gt
from itertools import takewhile, count
import functools as fcn


def create_migrations(topology):
    '''
    Create functions used for transferring individuals from
    one islands to another, creates tuple of tuples.

    topology - directed graph representing connections between islands
    '''
    num_islands = len(topology)

# an airport receives individuals, it's a traffic stop for an islands
# for single process implementation, an airport is a simple list
    airports = [list() for _ in range(num_islands)]

    def generate_immigration(airport):
        def immigrate():
            immigrants = []
            while airport:
                immigrants.append(airport.pop())
            return tuple(immigrants)
        return immigrate

    immigrations = tuple(map(generate_immigration, airports))

    def generate_emmigration(idx):
        destination = airports[idx]
        def emmigrate(individual):
            destination.append(individual)
        return emmigrate

    emmigrations = tuple(tuple(generate_emmigration(neighbor_idx)
                               for neighbor_idx in neighbors)
                         for neighbors in topology)

    return immigrations, emmigrations


def create(operators, num_islands, population_size=20,
           degree=1, migration_size=1, migration_interval=200):
    ''' create archipelago, defaults to ring topology (degree=1) '''

    islands = [ga.island.create(operators, population_size)
               for _ in range(num_islands)]

    create_airports(islands, degree, migration_size, migration_interval)

    return islands


def evolution(evolve, immigration_policies, emmigration_policies):
    '''
    This is a Python generate which yields tuple of populations inhabiting
    abstract islands.
    '''
    num_islands = len(immigration_policies)

    islands = tuple(evolve() for _ in range(num_islands))

    for iteration in count():
        yield islands

# Immigration - Outside individuals are inhabiting an island
        islands = (immigrate(population) for (population, _), immigrate
                   in zip(islands, immigration_policies))

# Evolution - Each island population is evolved into the next generation
        islands = tuple(map(evolve, islands))

# Emmigration - Sends individuals (clones) from one population onto voyage
        for (population, _), migrate in zip(islands, emmigration_policies):
            migrate(population)
