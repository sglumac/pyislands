'''
Module containing an implementation of steady-state genetic algorithm.
'''
from pyislands.selection import ktournament
from pyislands.ga import create_population

import functools as fcn


def get_evolution(generate, crossover, mutate, evaluate, population_size):
    '''
    Returns closure evolve:
        evolve - uses crossover, mutate and evaluate to evolve some population
               - steady state iteration, uses 3-tournament selection

    population_k = evolve(population_k-1)
    '''

    return fcn.partial(__evolve, generate, crossover, mutate,
                       evaluate, population_size)


def __update_info(info):
    ''' evolution of information '''
# This dictionary determines information update (specific for this function)
# evals = 2 for comparing crossover children, 1 after mutation
    info_dict = {'individuals': lambda n: n + 1,
                 'evaluations': lambda n: n + 3}

    new_info = tuple(((k, info_dict[k](v)) for k, v in info))

    return new_info


def __evolve(generate, crossover, mutate, evaluate, population_size,
             population=None, info=None):
    '''
    This function uses crossover, mutate and evalute, functions
    passed as arguments to get_steady_evolve.
    '''

# Initial Population
    if population is None:
        return create_population(generate, evaluate, population_size)

# Selection = 3-Tournament
    individuals, idxs = ktournament(population, 3)
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

    return tuple(new_population), __update_info(info)
