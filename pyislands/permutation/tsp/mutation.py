import random
import functools as fcn
from itertools import islice, chain, combinations


def get_twoopt_mutation(adjacency_matrix, mutation_probability):
    return fcn.partial(__twoopt_mutation, adjacency_matrix,
                       mutation_probability)


def __twoopt_mutation(adjacency_matrix, mutation_probility, genotype):
    '''
    After each valid exchange_cost(i, j), tsp_cycle:

    city_0, city_1, city_2, ..., city_i-1, city_i, ... city_j-1, city_j, ...,
    city_n-1, city_0

    becomes

    city_0, city_1, city_2, ..., city_i-1, city_j, city_j-1, ..., city_i,
    city_j+1..., city_n-1, city_0
    '''

    if not random.random() < mutation_probility:
        return genotype

    tsp_cycle = list(chain([0], genotype, [0]))
    n = len(tsp_cycle)

    distance = lambda idx1, idx2: adjacency_matrix[tsp_cycle[idx1]][tsp_cycle[idx2]]

    def exchange_cost(i, j):

        removed_cost = distance(i - 1, i) + distance(j - 1, j)
        added_cost = distance(i - 1, j - 1) + distance(i, j)

        return added_cost - removed_cost

    exchange = True
    idxs = range(1, n - 1)
    while exchange:
        exchange = False
        for i, j in combinations(idxs, 2):
            if j > i + 1 and exchange_cost(i, j) < 0:

                tsp_cycle = list(chain(islice(tsp_cycle, 0, i),
                                       reversed(tsp_cycle[i:j]),
                                       islice(tsp_cycle, j, n)))
                exchange = True

    new_genotype = tuple(islice(tsp_cycle, 1, n - 1))

    return new_genotype
