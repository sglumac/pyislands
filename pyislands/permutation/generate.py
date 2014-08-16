from random import shuffle

def random_permutation(num_elements):
    tmp = range(1, num_elements)
    shuffle(tmp)

    return tuple(tmp)

def unit(num_elements):
    return tuple(range(1, num_elements + 1))
