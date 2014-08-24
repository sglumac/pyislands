from pyislands.permutation.generate import get_random_permutation_generator
from pyislands.permutation.generate import unit


def test_random_permutation():
    ''' This function asserts containing elements in permutation mutation '''
    elements = list(range(5, 20))
    generate = get_random_permutation_generator(elements)

    genotype = generate()

    for i in elements:
        assert i in genotype


def test_unit():
    ''' This function asserts containing elements in permutation mutation '''

    for i in unit(10):
        assert i in range(10)
