from pyislands.permutation.tsp.mutation import get_twoopt_mutation
from pyislands.permutation.tsp.graph import generate_graph, random_cities
from pyislands.permutation.tsp.graph import evaluate_path

def create_random_twoopt():
    adjacency_matrix = generate_graph(random_cities(10))

    two_opt = get_twoopt_mutation(adjacency_matrix, 1.0)

    return two_opt, adjacency_matrix


def test1_two_opt():
    two_opt, _ = create_random_twoopt()
    genotype = range(1, 10)
    new_genotype = two_opt(genotype)

    for i in genotype:
        assert i in new_genotype


def test1_two_opt():
    two_opt, adjacency_matrix = create_random_twoopt()
    genotype = range(1, 10)

    new_genotype = two_opt(genotype)

    evaluate = lambda g: evaluate_path(adjacency_matrix, [0] + list(g) + [0])

    assert evaluate(new_genotype) < evaluate(genotype)




