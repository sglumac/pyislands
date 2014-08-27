import random
import functools as fcn


def get_emmigration(policy, migration_size, destinations):
    '''
    This function returns emmigrate function:
        emmigrate(population)
    '''
    return fcn.partial(policy, migration_size, destinations)


def random_policy(migration_size, destinations, population):
    '''
    This policy chooses random individuals for migration and
    random destination for each of these individuals.

    After emmigration there are two copies of one individual, one
    in the original population and the other at the destination.
    '''

    emmigrants = random.sample(population, migration_size)

    for individual in emmigrants:
        destination = random.choice(destinations)
        destination.put(individual)
        emmigrate(individual)
