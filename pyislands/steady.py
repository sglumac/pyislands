'''
steady state algorithm
'''
from random import sample


def ktournament(population, k):
    '''
    randomly select k-individuals from the population
    and sort them by penalty in the increasing order
    '''
    enumerated_population = [(individual, idx) for idx, individual in
                             enumerate(population)]
    individuals, idxs = zip(*sorted(sample(enumerated_population, k)))
    return individuals, idxs


def generate_population(generate, evaluate, num_individuals):
    '''
    generates num_individuals in population
    '''
    genotypes = (generate() for _ in range(num_individuals))
    population = tuple((evaluate(genotype), genotype)
                       for genotype in genotypes)

    return population


def iteration(crossover, mutate, evaluate, population):
    '''
    steady state iteration, uses 3-tournament selection
    (ensures 2-elitism)
    '''
# Selection = 3-Tournament
    individuals, idxs = ktournament(population, 3)
    parents = individuals[0:2]
    bad_idx = idxs[2]

# Crossover
    genotype1, genotype2 = (genotype for _, genotype in parents)
    children = crossover(genotype1, genotype2)
    best_genotype = min(children, key=evaluate)

# Mutation
    new_genotype = mutate(best_genotype)
    penalty = evaluate(new_genotype)

    child = (penalty, new_genotype)

# Replace bad individual
    new_population = list(population)
    new_population[bad_idx] = child

    return tuple(new_population)
