from random import shuffle

def random(num_elements):
    tmp = range(num_elements)
    shuffle(tmp)

    return tuple(tmp)

def unit(num_elements):
    return tuple(range(num_elements))
