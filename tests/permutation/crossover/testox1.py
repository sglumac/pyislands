from pyislands.permutation.crossover.ox1 import order_merge, order_crossover1


def test_order_merge_ox1():
    parent1 = (1, 2, 3, 4, 5, 6, 7, 8)
    parent2 = (2, 4, 6, 8, 7, 5, 3, 1)

    num_genes = len(parent1)

    break1, break2 = 2, 5

    swath1, swath2 = parent1[break1:break2], parent2[break1:break2]

    child1 = order_merge(swath1, parent2, break1, break2, num_genes)
    child2 = order_merge(swath2, parent1, break1, break2, num_genes)

    assert child1 == (8, 7, 3, 4, 5, 1, 2, 6)
    assert child2 == (4, 5, 6, 8, 7, 1, 2, 3)


def test_pmx():
    parent1_genotype = (0, 1, 2, 3, 4, 5, 6)
    parent2_genotype = (6, 4, 0, 2, 1, 5, 3)

    children_genotypes = order_crossover1(parent1_genotype, parent2_genotype)

    for genotype in children_genotypes:
        for i in parent1_genotype:
            assert i in genotype
