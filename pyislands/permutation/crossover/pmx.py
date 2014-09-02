import random
from itertools import islice, chain


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
