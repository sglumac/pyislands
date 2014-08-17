from itertools import takewhile
from selection import ktournament
import operator


def generate_population(generate, evaluate, num_individuals):
    '''
    generates num_individuals in population
    '''
    genotypes = (generate() for _ in range(num_individuals))
    population = tuple((evaluate(genotype), genotype)
                       for genotype in genotypes)

    return population


def evolution(generate, evolve):
    '''
    generator for populations during evolution

    new_population = generate() - creates population
    new_population = evolve(population) - evolves population
    '''
    population = generate()
    while True:
        yield population
        population = evolve(population)


def simple_info(iteration, population):
    ''' information about current algorithm iteration to stdout '''
    least_penalty, best_genotype = min(population)
    print "iteration =", iteration,
    print "penalty =", least_penalty



def get_solution(evolution, num_iterations, info=None):
    ''' get solution with info '''

    running = lambda en: en[0] < num_iterations

    for iteration, population in takewhile(running, enumerate(evolution())):
        if info:
            info(iteration, population)

    penalty, solution = min(population)

    return solution, penalty


def steady_evolve(crossover, mutate, evaluate, population):
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
    children_genotypes = crossover(genotype1, genotype2)
    best_genotype = min(children_genotypes, key=evaluate)

# Mutation
    new_genotype = mutate(best_genotype)
    penalty = evaluate(new_genotype)

    child = (penalty, new_genotype)

# Replace bad individual
    new_population = list(population)
    new_population[bad_idx] = child

    return tuple(new_population)
