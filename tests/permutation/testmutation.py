from pyislands.permutation.mutation import reversed_sequence_mutation
from pyislands.permutation.mutation import every_city_mutation
from pyislands.permutation.mutation import every_city_mutation2

from functools import partial


def check_mutation(mutation):
    genotype = range(10)

    new_genotype = mutation(genotype)

    for i in genotype:
        assert i in new_genotype


def test_rsm():
    check_mutation(partial(reversed_sequence_mutation, 1.0))


def test_ecm():
    check_mutation(partial(every_city_mutation, 1.0))


def test_ecm2():
    check_mutation(partial(every_city_mutation2, 1.0))
