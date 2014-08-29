import random
import functools as fcn

def get_every_city_mutation(mutation_probability):
    '''
    Exchange Every City - each with given probability
    '''

    return fcn.partial(__every_city_mutation, mutation_probability)


def __every_city_mutation(mutation_probability, genotype):
    num_genes = len(genotype)
    new_genotype = list(genotype)

    idxs = range(num_genes)
    for _ in idxs:
        if random.random() < mutation_probability:
            i, j = random.sample(idxs, 2)
            new_genotype[i], new_genotype[j] = new_genotype[j], new_genotype[i]

    return tuple(new_genotype)


def get2_every_city_mutation(mutation_probability):
    '''
    Exchange Every City - each with given probability
    '''

    return fcn.partial(__every_city_mutation2, mutation_probability)


def __binomial(n, p):
    ''' innefective binomial distribution '''
    return sum(random.random() < p for _ in range(n))


def __every_city_mutation2(mutation_probability, genotype):
    num_genes = len(genotype)
    new_genotype = list(genotype)

    num_exchanged = __binomial(num_genes - 1, mutation_probability)
    idxs = random.sample(range(num_genes), num_exchanged)

    for i, j in zip(idxs, sorted(idxs)):
        new_genotype[i], new_genotype[j] = new_genotype[j], new_genotype[i]

    return tuple(new_genotype)
