'''
This module contains examples of solving a random travelling salesman
problem using pyislands.
'''
from pyislands import ga
from pyislands import archipelago
from pyislands import island
from pyislands.types import Island

from pyislands.archipelago import topology
from pyislands.archipelago import form_destinations
from pyislands.archipelago import assimilation
from pyislands.archipelago.assimilation import get_immigration
from pyislands.archipelago import migration
from pyislands.archipelago.migration import get_emmigration

from pyislands.selection import get_ranking_select
from pyislands.permutation.generate import get_random_permutation_generator
from pyislands.permutation.mutation.rsm import get_reversed_sequence_mutation
from pyislands.permutation.crossover.ox1 import order_crossover1
import pyislands.permutation.tsp.graph as tsp

from itertools import chain
import functools as fcn


def evaluate_tsp(adjacency_matrix, genotype):
    return tsp.evaluate_path(adjacency_matrix, [0] + list(genotype) + [0])

def generate_tsp_evolution(adjacency_matrix, num_cities):
    '''
    This function defines algorithm used for solving a travelling salesman
    problem. Algorithm parameters are hardcoded into this function, it is just
    an example.
    '''

    population_size = 10
    mutation_probability = 0.8

    evaluate = fcn.partial(evaluate_tsp, adjacency_matrix)

    elements = list(range(1, num_cities))
    generate = get_random_permutation_generator(elements)

    mutate = get_reversed_sequence_mutation(mutation_probability)

    crossover = order_crossover1

    get_select = fcn.partial(get_ranking_select, 0.5)
    evolve = ga.generational.get_elitist_evolution(get_select, crossover, mutate, evaluate)

    create_population = fcn.partial(island.create_population, generate, evaluate,
                         population_size)

    return create_population, evolve


def solve_tsp_classic(adjacency_matrix, num_cities, num_iterations=20000):
    '''
    This functions runs a simple genetic algorithm which evolves a solution of
    a travelling salesman problem. It shows how to print out simple diagnostic
    for population.
    '''

# Simple Genetic Algorithm
    create_population, evolve = generate_tsp_evolution(adjacency_matrix, num_cities)

    best, _ = island.get_stagnation_solution(Island(create_population, evolve,
                                            None, None, None), 100)

    return tuple(chain([0], best.genotype, [0])), best.penalty


def solve_tsp_islands(adjacency_matrix, num_cities,
                      num_iterations=10000, use_multiprocess=False):
    '''
    This functions runs an island genetic algorithm which evolves a solution of
    a travelling salesman problem. It shows how to print out simple diagnostic
    for population.
    '''

    num_islands = 4
    migration_size = 1
    migration_interval = 1
    degree = 1

# Simple Genetic Algorithm
    create_population, evolve = generate_tsp_evolution(adjacency_matrix, num_cities)

# Migration Setup
    airports = \
        archipelago.multiprocess.create_airports(num_islands) \
        if use_multiprocess else \
        archipelago.nonparallel.create_airports(num_islands)


    migration_graph = topology.generate_regular(num_islands, degree)  # Ring topology

    destinations = form_destinations(migration_graph, airports)

    immigrations = \
        tuple(get_immigration(airport, assimilation.policy_2tournament)
              for airport in airports)

    emmigrations = \
        tuple(get_emmigration(migration.random_policy, migration_size, island_destinations)
              for island_destinations in destinations)

    #immigrations = (None,) * num_islands
    #emmigrations = (None,) * num_islands
    islands = tuple(Island(create_population, evolve,
                           immigrate, emmigrate, migration_interval)
                    for immigrate, emmigrate in zip(immigrations, emmigrations))

    penalty, solution = \
        archipelago.multiprocess.get_solution(islands, num_iterations) \
        if use_multiprocess else \
        archipelago.nonparallel.get_solution(islands, num_iterations)

    return tuple(chain([0], solution, [0])), penalty


def main_tsp(num_cities=100, use_islands=False, use_multiprocess=False):
    '''
    This functions creates a random travelling salesman problem and
    solves it using classical or island model genetic algorithm.
    '''
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    if use_islands:
        solution, penalty = solve_tsp_islands(adjacency_matrix, num_cities,
                                              use_multiprocess=use_multiprocess)
    else:
        solution, penalty = solve_tsp_classic(adjacency_matrix, num_cities)

    print("solution = {0}".format(solution))
    print("penalty = {0}".format(penalty))


if __name__ == '__main__':
    main_tsp(500, False, False)
