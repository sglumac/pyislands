'''
Module contains permutation mutations. Mutation is function
with signature:

    def mutation(mutation_probability, penalty_function, parent):
        ...
        return child

'''
import random


def get_reversed_sequence_mutation(mutation_probability):
    '''
    Reversed Sequence Mutation - ignored with
    probability (1 - mutation_probability)
    '''

    def reversed_sequence_mutation(genotype):
        new_genotype = list(genotype)

        if random.random() < mutation_probability:
            num_genes = len(genotype)
            break1, break2 = sorted(random.sample(range(num_genes + 1), 2))
            new_genotype[break1:break2] = reversed(genotype[break1:break2])

        return tuple(new_genotype)

    return reversed_sequence_mutation


def get_every_city_mutation(mutation_probability):
    '''
    Exchange Every City - each with given probability
    '''

    def every_city_mutation(genotype):
        num_genes = len(genotype)
        new_genotype = list(genotype)

        idxs = range(num_genes)
        for _ in idxs:
            if random.random() < mutation_probability:
                i, j = random.sample(idxs, 2)
                new_genotype[i], new_genotype[j] = new_genotype[j], new_genotype[i]

        return tuple(new_genotype)

    return every_city_mutation


def binomial(n, p):
    ''' innefective binomial distribution '''
    return sum(random.random() < p for _ in range(n))


def get2_every_city_mutation(mutation_probability):
    '''
    Exchange Every City - each with given probability
    '''

    def every_city_mutation(genotype):
        num_genes = len(genotype)
        new_genotype = list(genotype)

        num_exchanged = binomial(num_genes - 1, mutation_probability)
        idxs = random.sample(range(num_genes), num_exchanged)

        for i, j in zip(idxs, sorted(idxs)):
            new_genotype[i], new_genotype[j] = new_genotype[j], new_genotype[i]

        return tuple(new_genotype)

    return every_city_mutation
