'''
Synchronous Island creation for testing on a single computer,
this module connects populations/islands using simple queues/lists.
'''
import random
from operator import itemgetter


def create_migrations(topology):
    '''
    Create functions used for transferring individuals from
    one islands to another, creates tuple of tuples.

    topology - directed graph representing connections between islands
    '''
    num_islands = len(topology)

# an airport receives individuals, it's a traffic stop for an islands
# for single process implementation, an airport is a simple list
    airports = [list() for _ in range(num_islands)]

    def generate_immigration(airport):
        def immigrate():
            immigrants = []
            while airport:
                immigrants.append(airport.pop())
            return tuple(immigrants)

    immigrations = tuple(map(generate_immigration, airports))

    def generate_emmigration(idx):
        destination = airports[idx]
        def emmigrate(individual):
            destination.append(individual)

    emmigrations = tuple(tuple(generate_emmigration(neighbor_idx)
                               for neighbor_idx in neighbors)
                         for neighbors in topology)

    return immigrations, emmigrations



def create(operators, num_islands, population_size=20,
           degree=1, migration_size=1, migration_interval=200):
    ''' create archipelago, defaults to ring topology (degree=1) '''

    islands = [ga.island.create(operators, population_size)
               for _ in range(num_islands)]

    create_airports(islands, degree, migration_size, migration_interval)

    return islands


def get_solution(island_evolutions, num_iterations, info=None):
    '''
    run synchronous genetic algorithm on all islands
    and get a solution
    '''

    evolutions = [evolution() for evolution in island_evolutions]


    for evolution in evolutions:
        iteration, population = evolution.next()
        if info:
            info(iteration, population)


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
