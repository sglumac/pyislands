import random
import functools as fcn


def get_random_permutation_generator(elements):
    '''
    Generates closure around elements = (x_0, x_1, x_2, ..., x_n-1). This
    closure returns random permutation of this elements,
    e.g. (x_0, x_n-1, x_3, ..., x_2, x_n - 1)
    '''

    generator_elements = list(elements)

    return fcn.partial(__random_permutation_generator, generator_elements)


def __random_permutation_generator(generator_elements):
    ''' Closure which returns permutation of generator_elements '''

    random.shuffle(generator_elements)

    return tuple(generator_elements)


def unit(num_elements):
    ''' generates unit permutation, (0, 1, 2, ..., n - 1) '''
    return tuple(range(num_elements))
