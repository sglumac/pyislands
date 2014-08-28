from pyislands.permutation.crossover import cyclic_crossover
from pyislands.permutation.crossover import partially_mapped_crossover
from pyislands.permutation.crossover import pmx_find


def test_cx1():
    parent1 = (8, 4, 7, 3, 6, 2, 5, 1, 9, 0)
    parent2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    child1, child2 = cyclic_crossover(parent1, parent2)

    assert child1 == (8, 1, 2, 3, 4, 5, 6, 7, 9, 0)
    assert child2 == (0, 4, 7, 3, 6, 2, 5, 1, 8, 9)


def test_cx2():
    parent1 = (0, 1, 2, 3, 4, 5, 6)
    parent2 = (6, 4, 0, 2, 1, 5, 3)

    child1, child2 = cyclic_crossover(parent1, parent2)

    assert child1 == (0, 4, 2, 3, 1, 5, 6)
    assert child2 == (6, 1, 0, 2, 4, 5, 3)


def test_pmx():
    parent1_genotype = (0, 1, 2, 3, 4, 5, 6)
    parent2_genotype = (6, 4, 0, 2, 1, 5, 3)

    children_genotypes = partially_mapped_crossover(parent1_genotype, parent2_genotype)

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
