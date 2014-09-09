'''
This module contains examples of solving a random travelling salesman
problem using pyislands.
'''
from pyislands import ga
from pyislands.creation import get_create_population

from pyislands.selection import get_ranking_select
from pyislands.permutation.generate import get_number_permutation_generator
from pyislands.permutation.mutation.rsm import get_reversed_sequence_mutation
from pyislands.permutation.crossover.ox1 import order_crossover1
import pyislands.permutation.tsp.graph as tsp

import functools as fcn


def generate_tsp_evolution(population_size, selection_pressure,
                           mutation_probability, adjacency_matrix):
    '''
    This function defines algorithm used for solving a travelling salesman
    problem. Algorithm parameters are hardcoded into this function, it is just
    an example.
    '''

    evaluate = tsp.get_evaluate_cycle(adjacency_matrix)

    generate = get_number_permutation_generator(1, len(adjacency_matrix))

    mutate = get_reversed_sequence_mutation(mutation_probability)

    crossover = order_crossover1

    get_select = fcn.partial(get_ranking_select, selection_pressure)
    evolve = ga.generational.get_elitist_evolution(get_select, crossover, mutate, evaluate)

    create_population = get_create_population(generate, evaluate, population_size)

    return create_population, evolve
