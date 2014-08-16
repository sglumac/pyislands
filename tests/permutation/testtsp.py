from pyislands.permutation.tsp import generate_graph, evaluate_path
from nose.tools import assert_almost_equals
from math import sqrt
import functools as fcn


class TestTSPGraphSimple:

    def __init__(self):
        cities = [(0.0, 0.0), (1.0, 0.0)]
        self.adjacency_matrix = generate_graph(cities)

    def test_distance(self):
        d1 = self.adjacency_matrix[0][1]
        d2 = self.adjacency_matrix[1][0]
        assert_almost_equals(d1, 1.0)
        assert_almost_equals(d2, 1.0)

    def test_evaluate_cycle(self):
        evaluate = fcn.partial(evaluate_path, self.adjacency_matrix)

        length1 = evaluate([0, 1])
        assert_almost_equals(length1, 1.0)

        length2 = evaluate([0, 1, 0])
        assert_almost_equals(length2, 2.0)

        length3 = evaluate([1, 0])
        assert_almost_equals(length3, 1.0)

        length4 = evaluate([1, 0, 1])
        assert_almost_equals(length4, 2.0)


class TestTSPGraphMedium:
    '''
    test done on three cities
    '''

    def __init__(self):
        cities = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
        self.adjacency_matrix = generate_graph(cities)

    def test_distance(self):
        test_edges = {(0, 1): 1.0, (1, 2): 1.0, (2, 0): sqrt(2.0)}

        for (city1, city2) in test_edges:
            distance = self.adjacency_matrix[city1][city2]
            assert_almost_equals(distance, test_edges[(city1, city2)])

    def test_evaluate_path(self):
        evaluate = fcn.partial(evaluate_path, self.adjacency_matrix)

        length = evaluate([0, 1, 2, 0])
        assert_almost_equals(length, 2.0 + sqrt(2.0))

        length = evaluate([2, 1, 0, 2])
        assert_almost_equals(length, 2.0 + sqrt(2.0))
