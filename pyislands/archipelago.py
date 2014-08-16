'''
Synchronous Island creation for testing on a single computer
'''
import ga
from ga.selection import ktournament
from ga.utility import replace, check_best

import random
from operator import itemgetter
from itertools import izip, imap


def generate_topology(num_islands, degree):
    '''
    Creates a directed, regular, fully connected graph with
    given degree of each vertex/island. This function is used
    for creating migration topology, return its adjacency list.
    '''
    island_ids = range(num_islands)
    neighbors = [island_ids[-i:] + island_ids[:-i]
                 for i in range(degree, 0, -1)]

    return list(izip(*neighbors))


def create_airports(islands, degree, migration_size, migration_interval):
    ''' adjacency matrix is given for airport topology '''

    airports = [{'migration_size': migration_size,
                 'migration_interval': migration_interval,
                 'individuals': list()}
                for _ in islands]

    topology = generate_topology(len(islands), degree)

    for island, airport, destination_idxs in izip(islands, airports, topology):
        airport['destinations'] = [airports[i] for i in destination_idxs]
        island['airport'] = airport


def receive_immigration(island):
    ''' immigration policy of some population '''
    population = island['population']
    immigrants = island['airport']['individuals']
    while immigrants:
        immigrant = immigrants.pop()
        _, bad = ktournament(population, 2)
        replace(bad, immigrant)
        check_best(island, immigrant)


def send_emmigration(island):
    '''
    randomly choses individuals for emmigration, its up to
    the programmer to schedule the migration interval
    '''
    population = island['population']
    destinations = island['airport']['destinations']
    emmigrants = random.sample(population, island['airport']['migration_size'])
    for emmigrant in emmigrants:
        destination = random.choice(destinations)
        destination['individuals'].append(emmigrant)


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

    return min((island['best'] for island in islands),
               key=itemgetter('penalty'))


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

    return min((island['best'] for island in islands),
               key=itemgetter('penalty'))
