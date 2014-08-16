from pyislands.permutation.crossover import cyclic_crossover
from pyislands.permutation.crossover import partially_mapped_crossover


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
