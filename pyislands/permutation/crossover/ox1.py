import random
from itertools import chain, islice


def order_merge(swath, parent2, break1, break2, num_genes):
    ''' merge order '''
    swath_set = set(swath)
    in_swath = lambda gene: gene not in swath_set

    inv_parent2 = chain(islice(parent2, break2, num_genes),
                        islice(parent2, break2))

    other_genes = list(filter(in_swath, inv_parent2))

    child = tuple(chain(islice(other_genes, num_genes - break2,
                               num_genes - break2 + break1),
                        swath,
                        islice(other_genes, num_genes - break2)))
    return child


def order_crossover1(parent1, parent2):
    '''
    Cyclic Crossover
    '''
    num_genes = len(parent1)

    break1 = random.randrange(num_genes)
    break2 = (break1 + random.randrange(num_genes)) % num_genes
    if break1 > break2:
        break1, break2 = break2, break1

    swath1, swath2 = parent2[break1:break2], parent1[break1:break2]

    child1 = order_merge(swath1, parent2, break1, break2, num_genes)
    child2 = order_merge(swath2, parent1, break1, break2, num_genes)

    return child1, child2
