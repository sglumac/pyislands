import functools as fcn


def get_immigration(airport, policy):
    '''
    This function returns immigrate function:
        new_population = immigrate(population)
    '''
    return fcn.partial(__immigrate, policy, airport)


def __immigrate(policy, airport, population):
    '''
    Immigration imports all immigrants from the airport.
    The airport should support get, put and empty methods (e.g. Queue.Queue or
    multiprocessing.Queue).

    Immigrants are then mixed with the population using migration policy:
        new_population = policy(population, immigrants)
    '''

# import immigrants
    immigrants = []
    while not airport.empty():
        genotype = airport.get()
        immigrants.append(append)

# mix immigrants with the population
    new_population = policy(population, immigrants)

    return new_population


def policy_2tournament(population, immigrants):
    ''' immigration policy of some population '''

    new_population = list(population)

    for immigrant in immigrants:
        _, idxs = ktournament(population, 2)
        bad_idx = idxs[1]

        new_population[bad_idx] = immigrant

    return tuple(new_population)
