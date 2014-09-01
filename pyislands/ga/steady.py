'''
Module containing an implementation of steady-state genetic algorithm.
'''
from pyislands.selection import ktournament

import functools as fcn


def get_evolution(crossover, mutate, evaluate):
    '''
    Returns closure evolve:
        evolve - uses crossover, mutate and evaluate to evolve some population
               - steady state iteration, uses 3-tournament selection

    population_k = evolve(population_k-1)
    '''

    return fcn.partial(__evolve, crossover, mutate, evaluate)


def __evolve(crossover, mutate, evaluate, population):
    '''
    This function uses crossover, mutate and evalute, functions
    passed as arguments to get_steady_evolve.
    '''

# Selection = 3-Tournament
    individuals, idxs = ktournament(3, population)
    parent1, parent2, _ = individuals
    _, _, bad_idx = idxs

# Crossover
    _, genotype1 = parent1
    _, genotype2 = parent2
    children_genotypes = crossover(genotype1, genotype2)
    best_genotype = min(children_genotypes, key=evaluate)

# Mutation
    new_genotype = mutate(best_genotype)
    penalty = evaluate(new_genotype)

    child = (penalty, new_genotype)

# Replace bad individual
    new_population = list(population)
    new_population[bad_idx] = child

    return tuple(new_population)
