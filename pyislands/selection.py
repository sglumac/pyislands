'''
Module containing selection functions on population
'''
import random
from math import floor, sqrt

import functools as fcn


def ktournament(k, population):
    '''
    randomly select k-individuals from the population
    and sort them by penalty in the increasing order
    '''

    enumerated_population = list(enumerate(population))

# enumerated_individual = (idx, (penalty, genotype))
    selected_individuals = random.sample(enumerated_population, k)

    penalty = lambda enumerated_individual: enumerated_individual[1][0]

# individuals are sorted by penalty
    idxs, individuals = zip(*sorted(selected_individuals, key=penalty))

    return individuals, idxs


def __ranking_select(sp, population):
    ''' selects random individual with distribution (sp in [1, 2]) '''

    n = len(population)
    p = random.random()

    a = sp - 1
    b = (2 - sp) * n - 1
    c = -n * (n - 1) * p

    idx = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    idx = int(floor(idx))

    individual = population[idx]

    return individual


def get_ranking_select(selection_pressure, population):
    '''
    It sorts the population and returns a closure around __ranking_select
    function.  This closure returns a random individual from the population
    with distriburion based on penalty determined with selection_pressure.

    selection_pressure in [0, 1]:
        0 -> no selection pressure (each individual can be selected with equal
        probability)
        1 -> maximum selection pressure (the worst individual cannot be chosen)

    The probability of chosing index i in (0, 1, ..., n - 1) in the sorted
    population (sp in [1, 2]):
        p_i = (2 - sp  + 2 * (sp - 1) * i / (n - 1)) / n

        Marko Cupic, Prirodom inspirirani optimizacijski algoritmi
    '''

    sp = selection_pressure + 1

# the best individual has the largest index
    population = sorted(population, reverse=True)

    return fcn.partial(__ranking_select, sp, population)
