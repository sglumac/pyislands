from pyislands.permutation.mutation.rsm import get_reversed_sequence_mutation
from pyislands.permutation.mutation.ecm import get_every_city_mutation

from tests.permutation.mutation import check_mutation


def test_ecm():
    check_mutation(get_every_city_mutation(1.0))
