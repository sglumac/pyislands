'''
this module implements methods for receiving and
sending individuals from one island to another
'''
from pyislands.selection import ktournament

import random
from itertools import count


def get_random_emmigration_policy(emmigration, migration_size):
    '''
    randomly choses individuals for emmigration, its up to
    the programmer to schedule the migration interval
    '''

    def random_migration(population):
        emmigrants = random.sample(population, migration_size)

        for emmigrant in emmigrants:
            emmigrate = random.choice(emmigration)
            emmigrate(emmigrant)

    return random_migration


def get_2tournament_immigration_policy(immigrate):
    ''' immigration policy of some population '''

    def immigration(population, info):
        immigrants = immigrate()

        if not immigrants:
            return population, info

        new_population = list(population)

        for immigrant in immigrants:
            _, idxs = ktournament(population, 2)
            bad_idx = idxs[1]

            new_population[bad_idx] = immigrant

        return tuple(new_population), info

    return immigration

