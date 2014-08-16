import pyislands.steady as steady
from pyislands.steady import generate_population
from pyislands.permutation.generate import random_permutation
from pyislands.permutation.mutation import reversed_sequence_mutation
from pyislands.permutation.crossover import partially_mapped_crossover
import pyislands.permutation.tsp as tsp
import functools as fcn


def main(num_cities=100):
    
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    def evaluate(genotype):
        return tsp.evaluate_path(adjacency_matrix, [0] + list(genotype) + [0])

    generate = fcn.partial(random_permutation, num_cities)
    mutate = fcn.partial(reversed_sequence_mutation, 0.8)
    crossover = partially_mapped_crossover

    population_size = 10
    population = generate_population(generate, evaluate, population_size)

    evolve = fcn.partial(steady.iteration, crossover, mutate, evaluate)


    num_iterations = 20000
    for i in range(num_iterations):
        least_penalty, best_genotype = min(population)
        print "iteration =", i,
        print "penalty =", least_penalty
        population = evolve(population)


if __name__ == '__main__':
    main()

