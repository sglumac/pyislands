import pyislands.permutation.tsp as tsp
from pyislands.example import solve_tsp

from math import sqrt


def test_tsp():
    num_cities = 10
    cities = tsp.random_cities(num_cities)
    adjacency_matrix = tsp.generate_graph(cities)

    solution, penalty = solve_tsp(adjacency_matrix, num_cities, 200)

    assert sorted(solution) == [0] + list(range(num_cities))
    assert penalty <= num_cities * sqrt(2)
