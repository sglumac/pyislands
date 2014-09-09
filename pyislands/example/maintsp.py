from pyislands.example.evolvetsp import generate_tsp_evolution

from pyislands.types import Island, create_single_island
from pyislands.evolution import finite_evolution, stagnation_evolution

from pyislands import archipelago
from pyislands.archipelago import topology
from pyislands.archipelago import form_destinations
from pyislands.archipelago import assimilation
from pyislands.archipelago.assimilation import get_immigration
from pyislands.archipelago import migration
from pyislands.archipelago.migration import get_emmigration

import pyislands.permutation.tsp.graph as tsp

from itertools import chain


def solve_tsp_classic(adjacency_matrix, max_stagnation=100, population_size=10,
                      selection_pressure=0.5, mutation_probability=0.6):
    '''
    This functions runs a simple genetic algorithm which evolves a solution of
    a travelling salesman problem. It shows how to print out simple diagnostic
    for population.
    '''

# Simple Genetic Algorithm
    create_population, evolve = \
        generate_tsp_evolution(population_size, selection_pressure,
                               mutation_probability, adjacency_matrix)

    island = create_single_island(create_population, evolve)
    enumerated_evolution = enumerate(stagnation_evolution(max_stagnation, island))
    for iteration, population in enumerated_evolution:
        best = min(population)
        print("iter = {0}, penalty = {1}".format(iteration, best.penalty))

    return tuple(tsp.form_cycle(best.genotype)), best.penalty


def solve_tsp_islands(adjacency_matrix, num_iterations=10000, use_multiprocess=False):
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
    create_population, evolve = generate_tsp_evolution(10, 0.5, 0.8,
                                                       adjacency_matrix)

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

    islands = tuple(Island(create_population, evolve,
                           immigrate, emmigrate, migration_interval)
                    for immigrate, emmigrate in zip(immigrations, emmigrations))

    penalty, solution = \
        archipelago.multiprocess.get_solution(islands, num_iterations) \
        if use_multiprocess else \
        archipelago.nonparallel.get_solution(islands, num_iterations)

    return tuple(tsp.form_cycle(solution)), penalty


def main_tsp(num_cities=100, use_islands=False, use_multiprocess=False):
    '''
    This functions creates a random travelling salesman problem and
    solves it using classical or island model genetic algorithm.
    '''
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    if use_islands:
        solution, penalty = solve_tsp_islands(adjacency_matrix, 1000,
                                              use_multiprocess=use_multiprocess)
    else:
        solution, penalty = solve_tsp_classic(adjacency_matrix)

    print("solution = {0}".format(solution))
    print("penalty = {0}".format(penalty))


if __name__ == '__main__':
    main_tsp(500, True, True)
