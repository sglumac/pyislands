import random
from itertools import chain, islice


def cyclic_crossover(parent1, parent2):
    '''
    Cyclic Crossover
    '''
    num_genes = len(parent1)

    child1 = [-1] * num_genes
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
