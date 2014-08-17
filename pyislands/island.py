'''
this module implements methods for receiving and
sending individuals from one island to another
'''
from pyislands.selection import ktournament

import random


def send_random_migration(emmigrations, migration_size, population):
    '''
    randomly choses individuals for emmigration, its up to
    the programmer to schedule the migration interval
    '''
    emmigrants = random.sample(population, migration_size)

    for emmigrant in emmigrants:
        emmigrate = random.choice(emmigrations)
        emmigrate(emmigrant)


def receive_migration(immigrate, population):
    ''' immigration policy of some population '''
    new_population = list(population)
    immigrants = immigrate()

    while immigrants:
        immigrant = immigrants.pop()
        _, idxs = ktournament(population, 2)
        bad_idx = idxs[1]

        new_population[bad_idx] = immmigrant

    return tuple(new_population)


