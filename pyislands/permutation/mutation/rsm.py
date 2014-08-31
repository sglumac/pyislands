import random
import functools as fcn
from itertools import chain, islice


def get_reversed_sequence_mutation(mutation_probability):
    '''
    Reversed Sequence Mutation - ignored with
    probability (1 - mutation_probability)

    In tsp, equivalent to exchange of two edges.
    '''

    return fcn.partial(__reversed_sequence_mutation, mutation_probability)


def __reversed_sequence_mutation(mutation_probability, genotype):

    if not random.random() < mutation_probability:
        return genotype

    num_genes = len(genotype)
    break1, break2 = sorted(random.sample(range(num_genes + 1), 2))

    new_genotype = tuple(chain(islice(genotype, break1),
                               reversed(genotype[break1:break2]),
                               islice(genotype, break2, num_genes)))

    return new_genotype
