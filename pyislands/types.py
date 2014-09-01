from collections import namedtuple


Individual = namedtuple('Individual', ['penalty', 'genotype'])

Island = namedtuple('Island', ['create_population', 'evolve',
                               'immigrate', 'emmigrate'])


def create_individual(evaluate, genotype):
    ''' Utility function used for evaluating genotype '''

    penalty = evaluate(genotype)

    return Individual(penalty, genotype)
