from itertools import islice


def evolution(island):
    '''
    Infinite generator for evolution of some population.
    This generator yields population:
        population - tuple together containing tuples/individuals

    population_0 = create()
    population_1 = evolve(population_0, info_0)
    .
    .
    population_k = evolve(population_k-1, info_k-1)
    .
    .

    Since population is a tuple/an immutable type, a population cannot be
    influenced by outside functions. Population can be used only to gather
    statistics

    If no immigration and emmigration is used this island evolution
    becomes a classical genetic algorithm.
    '''

    population = island.create_population()

    while True:
        for _ in range(island.migration_interval if island.migrate else 1):
            yield population
# Immigration - Outside individuals are inhabiting an island
            if island.assimilate:
                population = island.assimilate(population)

# Evolution - Each island population is evolved into the next generation
            population = island.evolve(population)

# Emmigration - Sends individuals (clones) from one population onto voyage
        if island.migrate:
            island.migrate(population)


def finite_evolution(num_iterations, island):
    ''' Same as evolution, except stopped after num_iterations '''
    return islice(evolution(island), num_iterations)


def stagnation_evolution(max_stagnation, island):
    ''' Same as evolution, except stopped after max_stagnation '''

    infinite_evolution = evolution(island)

    population = next(infinite_evolution)

    best = min(population)

    stagnation = 0

    while stagnation < max_stagnation:
        stagnation += 1
        yield population
        population = next(infinite_evolution)

        current_best = min(population)
        if current_best < best:
            stagnation = 0
            best = current_best
