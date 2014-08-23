'''
module describing simple genetic algorithm
'''
from pyislands.selection import ktournament


def create_population(generate, evaluate, num_individuals):
    ''' generates num_individuals in population '''

    genotypes = (generate() for _ in range(num_individuals))

    create_individual = lambda genotype: (evaluate(genotype), genotype)

    population = tuple(map(create_individual, genotypes))

    return population


def evolution(create, evolve, investigate):
    '''
    Infinite generator for evolution of some population.
    This generator yields (population, info):
        population - tuple together containing tuples/individuals
        info - dictionary defined using investigate function

    population_0 = create()
    population_1 = evolve(population_0, info_0)
    .
    .
    population_k = evolve(population_k-1, info_k-1)
    .
    .

    info_0 = investigate(population_0)
    info_1 = investigate(population_1, info_0)
    .
    .
    info_k-1 = investigate(population_k-1, info_k-1)
    .
    .

    Since population is a tuple/an immutable type, a population cannot be
    influenced by outside functions. Population can be used only to gather
    statistics
    '''
    population = create()
    info = investigate(population)
    while True:
        yield population, info
        population = evolve(population, info)
        info = investigate(population, info)


def get_steady_evolve(crossover, mutate, evaluate):
    '''
    Returns closure evolve:
        evolve - uses crossover, mutate and evaluate to evolve some population
               - steady state iteration, uses 3-tournament selection

    population_k = evolve(population_k-1)
    '''

    def steady_evolve(population, dummy):

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

    return steady_evolve
