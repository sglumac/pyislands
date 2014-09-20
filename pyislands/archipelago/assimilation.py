from pyislands.selection import ktournament

import functools as fcn


def get_assimilation(airport, policy):
    '''
    This function returns assimilate function:
        new_population = assimilate(population)
    '''
    return fcn.partial(__assimilate, policy, airport)


def __assimilate(policy, airport, population):
    '''
    Assimilation imports all immigrants from the airport.
    The airport should support get, put and empty methods (e.g. Queue.Queue or
    multiprocessing.Queue).

    Immigrants are then mixed with the population using migration policy:
        new_population = policy(population, immigrants)
    '''

# import immigrants
    immigrants = []
    while not airport.empty():
        genotype = airport.get()
        immigrants.append(genotype)

# mix immigrants with the population
    new_population = policy(population, immigrants)

    return new_population


def policy_2tournament(population, immigrants):
    ''' assimilation policy of some population '''

    new_population = list(population)

    for immigrant in immigrants:
        _, idxs = ktournament(2, population)
        bad_idx = idxs[1]

        new_population[bad_idx] = immigrant

    return tuple(new_population)
