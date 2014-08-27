import multiprocessing


def create_airports(num_islands):
    '''
    An airport is a traffic stop for an islands. An airport
    should support get, put and empty operations. Queues
    are used as an implementation of an airport.
    '''

    manager = multiprocessing.Manager()
    airports = tuple(Queue() for _ in range(num_islands))

    return airports



def get_solution(

def evolution(island):
    '''
    This is a Python generate which yields tuple of populations inhabiting
    abstract islands.
    '''
    evolves, immigrations, emmigrations = zip(*islands)

# Since this is a single process implementation, populations are stored
# list, not on the separate islands (processes)
    populations = tuple(evolve() for evolve in evolves)

    while True:
        yield populations

# Immigration - Outside individuals are inhabiting an island
        populations = (immigrate(population) for immigrate, population
                       in zip(immigrations, populations))

# Evolution - Each island population is evolved into the next generation
        populations = tuple(evolve(population) for evolve, population
                            in zip(evolves, populations))

# Emmigration - Sends individuals (clones) from one population onto voyage
        for emmigrate, population in zip(emmigrations, populations):
            emmigrate(population)


evolution
