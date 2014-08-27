def evolution(evolve):
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
    population, info = evolve()
    while True:
        yield population, info
        population, info = evolve(population, info)


def create_population(generate, evaluate, population_size):
    '''
    This function is used in steady_evolve to create an initial
    population.
    '''
    genotypes = tuple(generate() for _ in range(population_size))
    penalties = map(evaluate, genotypes)
    population = tuple(zip(penalties, genotypes))

    return population


import pyislands.ga.steady
