'''
Module contains permutation crossovers. Crossover is function
with signature:

    def crossover(penalty_function, parent1, parent2):
        ...
        return children

where object children is list of individuals.
'''
import random
from itertools import chain


def cyclic_crossover(parent1, parent2):
    '''
    Cyclic Crossover
    '''
    num_genes = len(parent1)

    child1  = [-1] * num_genes
    child2 = [-1] * num_genes

    while -1 in child1:
        i = child1.index(-1)
        while parent2[i] not in child1:
            j = parent1.index(parent2[i])
            child1[j] = parent1[j]
            child2[j] = parent2[j]
            i = j
        parent1, parent2 = parent2, parent1

    return tuple(child1), tuple(child2)


def partially_mapped_crossover(parent1, parent2):
    '''
    Partially Mapped Crossover
    '''
    num_genes = len(parent1)

    child1 = list(parent1)
    child2 = list(parent2)

    break1 = random.randrange(num_genes + 1)
    tmp = random.randrange(num_genes)
    break2 = (break1 + tmp) % (num_genes + 1)
    if break1 > break2:
        break1, break2 = break2, break1

    child1[break1:break2], child2[break1:break2] = \
            child2[break1:break2], child1[break1:break2]
    swath1, swath2 = child1[break1:break2], child2[break1:break2]

    for i in chain(range(break1), range(break2, num_genes)):
        gen = child1[i]
        while gen in swath1:
            j = swath1.index(gen)
            gen = swath2[j]
        child1[i] = gen

        gen = child2[i]
        while gen in swath2:
            j = swath2.index(gen)
            gen = swath1[j]
        child2[i] = gen

    return tuple(child1), tuple(child2)
