'''
Module containing an implementation of steady-state genetic algorithm.
maybe BAD IMPLEMENTATION <- extra parents, extra children
'''
import functools as fcn


def get_evolution(get_select, crossover, mutate, evaluate):
    '''
    Returns closure evolve:
        evolve - uses get_select, crossover, mutate and evaluate
                 to evolve some population
               - generational iteration

    population_k = evolve(population_k-1)
    '''

    return fcn.partial(__evolve, get_select, crossover, mutate, evaluate)


def __evolve(get_select, crossover, mutate, evaluate, population):
    '''
    This function uses crossover, mutate and evalute, functions
    passed as arguments to get_steady_evolve.
    '''

    population_size = len(population)

# Selection
    select = get_select(population)

    mothers = (select() for _ in population)
    fathers = (select() for _ in population)

    mother_genotypes = (genotype for _, genotype in mothers)
    father_genotypes = (genotype for _, genotype in fathers)

# Crossover
    children_genotypes = map(crossover, mother_genotypes, father_genotypes)

# Mutation
    mutated_genotypes = map(mutate, children_genotypes)
    penalties = map(evaluate, mutated_genotypes)

    children = zip(penalties, mutated_genotypes)

# Replace bad individual
    new_population = tuple(islice(sorted(children), population_size))

    return new_population
