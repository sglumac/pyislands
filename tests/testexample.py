import pyislands.permutation.tsp.graph as tsp
from pyislands.example.maintsp import solve_tsp_classic, solve_tsp_islands

from math import sqrt


def test_tsp_classic():
    num_cities = 10
    num_iterations = 10
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    solution, penalty = solve_tsp_classic(adjacency_matrix, num_cities, 
                                          num_iterations)

    assert sorted(solution) == [0] + list(range(num_cities))
    assert penalty <= num_cities * sqrt(2)


def test_tsp_islands():
    num_cities = 10
    num_iterations = 10
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    solution, penalty = solve_tsp_islands(adjacency_matrix, num_cities,
                                          num_iterations)

    assert sorted(solution) == [0] + list(range(num_cities))
    assert penalty <= num_cities * sqrt(2)
