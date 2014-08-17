import pyislands.ga as ga
from pyislands.permutation.generate import random_permutation
from pyislands.permutation.mutation import reversed_sequence_mutation
from pyislands.permutation.crossover import partially_mapped_crossover
import pyislands.permutation.tsp as tsp

import functools as fcn
import random
from itertools import chain


def solve_tsp(adjacency_matrix, num_cities, num_iterations=20000):

    def evaluate(genotype):
        return tsp.evaluate_path(adjacency_matrix, [0] + list(genotype) + [0])

    def generate():
        genotype = list(range(1, num_cities))
        random.shuffle(genotype)
        return tuple(genotype)

    mutate = fcn.partial(reversed_sequence_mutation, 0.8)
    crossover = partially_mapped_crossover

    population_size = 10

    generate = fcn.partial(ga.generate_population, generate,
                           evaluate, population_size)
    evolve = fcn.partial(ga.steady_evolve, crossover, mutate, evaluate)

    evolution = fcn.partial(ga.evolution, generate, evolve)

    solution, penalty = ga.get_solution(evolution, num_iterations,
                                        ga.simple_info)

    return tuple(chain([0], solution, [0])), penalty


def main(num_cities=100):
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    solution, penalty = solve_tsp(adjacency_matrix, num_cities)

    print("solution =", solution)


if __name__ == '__main__':
    main()

