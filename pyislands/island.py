from itertools import islice
import os


def create_population(generate, evaluate, population_size):
    '''
    This function is used in steady_evolve to create an initial
    population.
    '''
    genotypes = tuple(generate() for _ in range(population_size))
    penalties = map(evaluate, genotypes)
    population = tuple(zip(penalties, genotypes))

    return population


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

    evolve, immigrate, emmigrate = island

    population = evolve()

    while True:
        yield population

# Immigration - Outside individuals are inhabiting an island
        if immigrate:
            population = immigrate(population)

# Evolution - Each island population is evolved into the next generation
        population = evolve(population)

# Emmigration - Sends individuals (clones) from one population onto voyage
        if emmigrate:
            emmigrate(population)


def get_solution(island, num_iterations):
    '''
    Utility function used for getting a solution from a single islands.
    '''

    for iteration, population in islice(enumerate(evolution(island)), num_iterations):
        least_penalty, _ = min(population)
        pid = os.getpid()
        print("pid = {0}, iteration = {1}, penalty = {2}".
              format(pid, iteration, least_penalty))

    penalty, solution = min(population)

    return solution, penalty
