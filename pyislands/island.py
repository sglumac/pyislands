'''
this module implements methods for receiving and
sending individuals from one island to another
'''
from pyislands.selection import ktournament

import random
from itertools import count


def emmigration_policy_random(emmigration, migration_size, population):
    '''
    randomly choses individuals for emmigration, its up to
    the programmer to schedule the migration interval
    '''
    emmigrants = random.sample(population, migration_size)

    for emmigrant in emmigrants:
        emmigrate = random.choice(emmigration)
        emmigrate(emmigrant)


def immigration_policy_2tournament(immigrate, population):
    ''' immigration policy of some population '''

    immigrants = immigrate()

    if not immigrants:
        return population

    new_population = list(population)

    while immigrants:
        immigrant = immigrants.pop()
        _, idxs = ktournament(population, 2)
        bad_idx = idxs[1]

        new_population[bad_idx] = immmigrant

    return tuple(new_population)


def evolution(generate_population, evolve, immigration_policy,
              emmigration_policy, migration_interval):
    '''
    generator for island during evolution

    new_population = generate_population()
    next_population = evolve(population)
    '''

    population = generate_population()

    for iteration in count():
        yield iteration, population

        population = immigration_policy(population)

        population = evolve(population)

        if iteration % migration_interval == 0:
            emmigration_policy(population)
