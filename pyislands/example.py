from pyislands import ga
from pyislands import island
from pyislands.archipelago import topology
import pyislands.archipelago.single_process as archipelago

from pyislands.permutation.generate import random_permutation
from pyislands.permutation.mutation import reversed_sequence_mutation
from pyislands.permutation.crossover import partially_mapped_crossover
import pyislands.permutation.tsp as tsp

import functools as fcn
import random
from itertools import chain


def generate_tsp_evolution(adjacency_matrix, num_cities):

    population_size = 10
    mutation_probability = 0.8

    def evaluate(genotype):
        return tsp.evaluate_path(adjacency_matrix, [0] + list(genotype) + [0])

    def generate():
        genotype = list(range(1, num_cities))
        random.shuffle(genotype)
        return tuple(genotype)

    mutate = fcn.partial(reversed_sequence_mutation, mutation_probability)

    crossover = partially_mapped_crossover

    generate = fcn.partial(ga.generate_population, generate,
                           evaluate, population_size)
    evolve = fcn.partial(ga.steady_evolve, crossover, mutate, evaluate)

    return generate, evolve


def solve_tsp_classic(adjacency_matrix, num_cities, num_iterations=20000):

    generate, evolve = generate_tsp_evolution(adjacency_matrix, num_cities)

    solution, penalty = ga.get_solution(generate, evolve, num_iterations,
                                        ga.simple_info)

    return tuple(chain([0], solution, [0])), penalty


def solve_tsp_islands(adjacency_matrix, num_cities, num_iterations=10000):

    num_islands = 4
    migration_size = 1
    migration_interval = 200
    degree = 1

    generate, evolve = generate_tsp_evolution(adjacency_matrix, num_cities)

    ring = topology.generate_regular(num_islands, degree)

    immigrations, emmigrations = archipelago.create_migrations(ring)

    immigration_policies = (fcn.partial(island.immigration_policy_2tournament,
                                        immigrate)
                            for immigrate in immigrations)

    emmigration_policies = (fcn.partial(island.emmigration_policy_random,
                                        emmigration, migration_size)
                            for emmigration in emmigrations)

    changes = tuple(fcn.partial(island.change, evolve, immigration_policy,
                                emmigration_policy, migration_interval)
                    for immigration_policy, emmigration_policy
                    in zip(immigration_policies, emmigration_policies))

    solution, penalty = archipelago.get_solution( \
            generate, changes, num_iterations, ga.simple_info)

    return tuple(chain([0], solution, [0])), penalty


def main_tsp(num_cities=100, use_islands=False):
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    if use_islands:
        solution, penalty = solve_tsp_islands(adjacency_matrix, num_cities)
    else:
        solution, penalty = solve_tsp_classic(adjacency_matrix, num_cities)

    print("solution = {0}".format(solution))


if __name__ == '__main__':
    main_tsp(use_islands=True)
