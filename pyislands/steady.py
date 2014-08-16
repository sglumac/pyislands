'''
steady state algorithm
'''
from ga.utility import replace, check_best
from ga.selection import ktournament


def evolution(generate, crossover, mutate, evaluate, population_size):
    '''
    algorithm uses steady state iteration, yields population each
    iteration and enables gathering statistics in between
    '''
    population = [generate() for _ in range(population_size)]

    while True:
        yield population
        population = iteration(crossover, mutate, evaluate, population)


def iteration(crossover, mutate, evaluate, population):
    '''
    steady state iteration, uses 3-tournament selection
    (ensures 2-elitism)
    '''
# Selection = 3-Tournament
    parent1, parent2, bad = ktournament(population, 3)
# Crossover
    children = crossover(parent1, parent2)
    child = min(children, key=evaluate)
# Mutation
    child = mutate(child)
    replace(bad, child)

    return population
