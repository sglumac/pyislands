'''
Module containing selection functions on population
'''
import random


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
