import random
import functools as fcn
from itertools import islice, chain, combinations


def get_twoopt_mutation(adjacency_matrix, mutation_probability):
    return fcn.partial(__twoopt_mutation, adjacency_matrix,
                       mutation_probability)


def __twoopt_mutation(adjacency_matrix, mutation_probility, genotype):

    if not random.random() < mutation_probility:
        return genotype

    tsp_cycle = list(chain([0], genotype, [0]))
    n = len(tsp_cycle)

    distance = lambda a, b: adjacency_matrix[tsp_cycle[a]][tsp_cycle[b]]

    def cost_exchange(i, j):

        removed_cost = distance(i - 1, i) + distance(j - 1, j)
        added_cost = distance(i - 1, j) + distance(j - 1, i)

        return removed_cost - added_cost

    exchange = True
    idxs = list(range(1, n - 1))
    while exchange:
        exchange = False
        for i, j in combinations(idxs, 2):
            if cost_exchange(i, j) < 0:
                tsp_cycle = list(chain(islice(tsp_cycle, 0, i),
                                       reversed(tsp_cycle[i:j + 1]),
                                       islice(tsp_cycle, j + 1, n)))

                exchange = True

    new_genotype = tuple(islice(tsp_cycle, 1, n - 1))

    return new_genotype
