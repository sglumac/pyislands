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


