from pyislands.permutation.mutation import get_reversed_sequence_mutation
from pyislands.permutation.mutation import get_every_city_mutation
from pyislands.permutation.mutation import get2_every_city_mutation


def check_mutation(mutation):
    genotype = range(10)

    new_genotype = mutation(genotype)

    for i in genotype:
        assert i in new_genotype


def test_rsm():
    check_mutation(get_reversed_sequence_mutation(1.0))


def test_ecm():
    check_mutation(get_every_city_mutation(1.0))


def test_ecm2():
    check_mutation(get2_every_city_mutation(1.0))
