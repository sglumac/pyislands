from collections import namedtuple
import functools as fcn


Individual = namedtuple('Individual', ['penalty', 'genotype'])

def create_individual(evaluate, genotype):
    ''' Utility function used for evaluating genotype '''

    penalty = evaluate(genotype)

    return Individual(penalty, genotype)
