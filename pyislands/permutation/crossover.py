'''
Module contains permutation crossovers. Crossover is function
with signature:

    def crossover(penalty_function, parent1, parent2):
        ...
        return children

where object children is list of individuals.
'''
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


def pmx_find(gen, swath1_dict):
    while gen in swath1_dict:
        gen = swath1_dict[gen]
    return gen


def gen_pmx_child(parent1, swath1, swath2, break1, break2, num_genes):

    swath1_dict = dict(zip(swath1, swath2))

    part1 = (pmx_find(gen, swath1_dict)
             for gen in islice(parent1, break1))
    part2 = (pmx_find(gen, swath1_dict)
             for gen in islice(parent1, break2, num_genes))

    return tuple(chain(part1, swath1, part2))


def partially_mapped_crossover(parent1, parent2):
    '''
    Partially Mapped Crossover
    '''
    num_genes = len(parent1)

    break1 = random.randrange(num_genes)
    break2 = (break1 + random.randrange(num_genes)) % num_genes
    if break1 > break2:
        break1, break2 = break2, break1

    swath1, swath2 = parent2[break1:break2], parent1[break1:break2]

    child1 = gen_pmx_child(parent1, swath1, swath2, break1, break2, num_genes)
    child2 = gen_pmx_child(parent2, swath2, swath1, break1, break2, num_genes)

    return child1, child2
