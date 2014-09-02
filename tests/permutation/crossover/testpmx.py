from pyislands.permutation.crossover.pmx import partially_mapped_crossover
from pyislands.permutation.crossover.pmx import pmx_find
from pyislands.permutation.crossover.pmx import gen_pmx_child


def test_pmx():
    parent1_genotype = (0, 1, 2, 3, 4, 5, 6)
    parent2_genotype = (6, 4, 0, 2, 1, 5, 3)

    children_genotypes = partially_mapped_crossover(parent1_genotype,
                                                    parent2_genotype)

    for genotype in children_genotypes:
        for i in parent1_genotype:
            assert i in genotype


def test_pmx_find():
    swath1 = (0, 1, 2, 3)
    swath2 = (1, 2, 3, 4)

    swath1_dict = dict(zip(swath1, swath2))
    swath2_dict = dict(zip(swath2, swath1))

    assert pmx_find(0, swath1_dict) == 4
    assert pmx_find(2, swath2_dict) == 0


def test_pmx_child():
    parent1 = (0, 1, 2, 3, 4, 5, 6)
    parent2 = (6, 4, 0, 2, 1, 5, 3)
    break1, break2 = 1, 6

    swath1, swath2 = parent2[break1:break2], parent1[break1:break2]

    child1 = gen_pmx_child(parent1, swath1, swath2, break1, break2,
                           len(parent1))

    assert child1 == (3, 4, 0, 2, 1, 5, 6)
