from random import shuffle

def random_permutation(num_elements):
    ''' generates random permutation, e.g. (0, n-1, 3, ..., 1, n - 1) '''
    tmp = list(range(num_elements))
    shuffle(tmp)

    return tuple(tmp)

def unit(num_elements):
    ''' generates unit permutation, (0, 1, 2, ..., n - 1) '''
    return tuple(range(num_elements))
