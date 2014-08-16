'''
steady state algorithm
'''
from random import sample
from operator import itemgetter


def ktournament(population, k):
    '''
    randomly select k-individuals from the population
    and sort them by penalty in the increasing order
    '''
    enumerated_population = ((individual, idx) for idx, individual in
                             enumerate(population))
    individuals, idxs = zip(*sorted(sample(enumerated_population, k)))
    return individuals, idxs


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
    individuals, idxs = ktournament(population, 3)
    parents = individuals[0:2]

# Crossover
    genotype1, genotype2 = (genotype for _, genotype in parents)
    children_genotypes = crossover(genotype1, genotype2)
    best_genotype = min(children_genotypes, key=evaluate)

# Mutation
    child_genotype = mutate(best_genotype)
    child_penalty = evaluate(child_genotype)

    child = (child_penalty, child_genotype)

# Replace bad individual
    new_population = population[:]
    new_population[idxs[2]] = child

    return new_population
