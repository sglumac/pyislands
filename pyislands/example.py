'''
This module contains examples of solving a random travelling salesman
problem using pyislands.
'''
from pyislands import ga
from pyislands import island
from pyislands.archipelago import topology
import pyislands.archipelago.single_process as archipelago

from pyislands.permutation.generate import get_random_permutation_generator
from pyislands.permutation.mutation import get_reversed_sequence_mutation
from pyislands.permutation.crossover import partially_mapped_crossover
import pyislands.permutation.tsp as tsp

from itertools import chain


def generate_tsp_evolution(adjacency_matrix, num_cities):
    '''
    This function defines algorithm used for solving a travelling salesman
    problem. Algorithm parameters are hardcoded into this function, it is just
    an example.
    '''

    population_size = 10
    mutation_probability = 0.8

    evaluate = lambda genotype: \
        tsp.evaluate_path(adjacency_matrix, [0] + list(genotype) + [0])

    elements = list(range(1, num_cities))
    generate = get_random_permutation_generator(elements)

    mutate = get_reversed_sequence_mutation(mutation_probability)

    crossover = partially_mapped_crossover

    evolve = ga.get_steady_evolve(generate, crossover, mutate,
                                  evaluate, population_size)

    return evolve


def solve_tsp_classic(adjacency_matrix, num_cities, num_iterations=20000):
    '''
    This functions runs a simple genetic algorithm which evolves a solution of
    a travelling salesman problem. It shows how to print out simple diagnostic
    for population.
    '''

# Simple Genetic Algorithm
    evolve = generate_tsp_evolution(adjacency_matrix, num_cities)
    evolution = ga.evolution(evolve)

# Main Loop
    for iteration, (population, dummy) in enumerate(evolution):
        least_penalty, _ = min(population)
        print("iteration = {0}, penalty = {1}".
              format(iteration, least_penalty))

# Termination Condition
        if iteration >= num_iterations:
            break

    penalty, solution = min(population)

    return tuple(chain([0], solution, [0])), penalty


def solve_tsp_islands(adjacency_matrix, num_cities, num_iterations=10000):
    '''
    This functions runs an island genetic algorithm which evolves a solution of
    a travelling salesman problem. It shows how to print out simple diagnostic
    for population.
    '''

    num_islands = 4
    migration_size = 1
    migration_interval = 200
    degree = 1

# Simple Genetic Algorithm
    evolve = generate_tsp_evolution(adjacency_matrix, num_cities)

# Migration Setup
    immigrations, emmigrations = \
        archipelago.create_migrations(num_islands, degree)

    immigration_policies = \
        tuple(island.get_2tournament_immigration_policy(immigrate)
              for immigrate in immigrations)

    emmigration_policies = \
        tuple(island.get_random_emmigration_policy(emmigration, migration_size)
              for emmigration in emmigrations)

    evolution = archipelago.evolution(evolve, immigration_policies, emmigration_policies)

# Main Loop
    for iteration, islands in enumerate(evolution):
        best_individuals = map(min, (population for population, info
                                     in islands))
        least_penalty, _ = min(best_individuals)
        print("iteration = {0}, penalty = {1}".
              format(iteration, least_penalty))
# Termination Condition
        if iteration >= num_iterations:
            break

    penalty, solution = min(map(min, (population for population, _ in islands)))
    return tuple(chain([0], solution, [0])), penalty


def main_tsp(num_cities=100, use_islands=False):
    '''
    This functions creates a random travelling salesman problem and
    solves it using classical or island model genetic algorithm.
    '''
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    if use_islands:
        solution, penalty = solve_tsp_islands(adjacency_matrix, num_cities)
    else:
        solution, penalty = solve_tsp_classic(adjacency_matrix, num_cities)

    print("solution = {0}".format(solution))
    print("penalty = {0}".format(penalty))


if __name__ == '__main__':
    main_tsp(use_islands=True)
