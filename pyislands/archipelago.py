'''
Synchronous Island creation for testing on a single computer,
this module connects island abstraction
'''
import ga
from ga.selection import ktournament
from ga.utility import replace, check_best

import random
from operator import itemgetter



def generate_topology(num_islands, degree):
    '''
    Creates a directed, regular, fully connected graph with
    given degree of each vertex/island. This function is used
    for creating migration topology, return its adjacency list.
    '''
    idxs = list(range(num_islands))
    neighbors = [idxs[-i:] + idxs[:-i] for i in range(degree, 0, -1)]

    return list(zip(*neighbors))


def create_migrations():
    '''
    create functions used for transferring individuals from
    one islands to another, creates tuple of tuplles
    '''
    pass


def create_airports(islands, degree, migration_size, migration_interval):
    ''' adjacency matrix is given for airport topology '''

    topology = generate_topology(len(islands), degree)

    for island, airport, destination_idxs in izip(islands, airports, topology):
        airport['destinations'] = [airports[i] for i in destination_idxs]
        island['airport'] = airport


def create(operators, num_islands, population_size=20,
           degree=1, migration_size=1, migration_interval=200):
    ''' create archipelago, defaults to ring topology (degree=1) '''

    islands = [ga.island.create(operators, population_size)
               for _ in range(num_islands)]

    create_airports(islands, degree, migration_size, migration_interval)

    return islands


def get_solution(islands, numiters=1000):
    '''
    run synchronous genetic algorithm on all islands
    and get a solution
    '''
    for iteration in range(numiters):
        for island in islands:
            print "iteration =", iteration,
            print "penalty =", island['best']['penalty']
            receive_immigration(island)
            ga.steady.iteration(island)
            if island['stats']['born'] % island['airport']['migration_interval'] == 0:
                send_emmigration(island)

    return min(min(population) for population in islands)


def get_stagnation_solution(islands, max_stagnation=1000):
    '''
    run synchronous genetic algorithm on all islands
    and get a solution
    '''
    stagnation = 0
    penalty = float('inf')
    while stagnation < max_stagnation:
        stagnation += 1
        for island in islands:
            receive_immigration(island)
            ga.steady.iteration(island)
            if island['stats']['born'] % island['airport']['migration_interval'] == 0:
                send_emmigration(island)

            next_penalty = min(island['best']['penalty'] for island in islands)
            if next_penalty < penalty:
                penalty = next_penalty
                stagnation = 0

    return min(min(population) for population in islands)
