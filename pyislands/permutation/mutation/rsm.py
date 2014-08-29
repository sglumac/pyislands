import random
import functools as fcn


def get_reversed_sequence_mutation(mutation_probability):
    '''
    Reversed Sequence Mutation - ignored with
    probability (1 - mutation_probability)
    '''

    return fcn.partial(__reversed_sequence_mutation, mutation_probability)


def __reversed_sequence_mutation(mutation_probability, genotype):
    new_genotype = list(genotype)

    if random.random() < mutation_probability:
        num_genes = len(genotype)
        break1, break2 = sorted(random.sample(range(num_genes + 1), 2))
        new_genotype[break1:break2] = reversed(genotype[break1:break2])

    return tuple(new_genotype)
