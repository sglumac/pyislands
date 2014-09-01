'''
Module containing an implementation of generational genetic algorithm.
'''
from pyislands.types import create_individual

import functools as fcn


def get_evolution(get_select, crossover, mutate, evaluate):
    '''
    Returns closure evolve:
        evolve - uses get_select, crossover, mutate and evaluate
                 to evolve some population
               - generational iteration

    population_k = evolve(population_k-1)
    '''

    return fcn.partial(__evolve, get_select, crossover, mutate, evaluate)


def __create_child(select, crossover, mutate, evaluate, dummy):
    ''' create one child '''

    mother, father = select(), select()

# Crossover
    children_genotypes = crossover(mother.genotype, father.genotype)
    best_genotype = min(children_genotypes, key=evaluate)

# Mutation
    new_genotype = mutate(best_genotype)

    child = create_individual(evaluate, new_genotype)

    return child


def __evolve(get_select, crossover, mutate, evaluate, population):
    '''
    This function uses crossover, mutate and evalute, functions
    passed as arguments to get_steady_evolve.

    Preserves one elite individual.
    '''

    select = get_select(population)

    create_child = fcn.partial(__create_child, select, crossover,
                               mutate, evaluate)

    children_population = map(create_child, population[:-1])

    best_individual = min(population)

    new_population = tuple(chain(children_population, [best_individual]))

    return new_population
