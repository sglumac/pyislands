from math import sqrt
from random import random


def generate_graph(cities):
    '''
    Generates Travelling Salesman's Graph (undirected graph)
    given cities salesman needs to visit

    cities  - [(x1, y1), (x2, y2), ..., (xn, yn)]
            - locations of n cities
            - n = len(cities)
    '''
    adjacency_matrix = \
            [[sqrt((x2-x1) ** 2 + (y2 - y1) ** 2) for (x1, y1) in cities]
             for (x2, y2) in cities]

    return adjacency_matrix


def evaluate_path(adjacency_matrix, tsp_path):
    '''
    function for evaluation of cycle given list

    tsp_path = [city1, city2, ..., cityn]
    '''
    return sum(adjacency_matrix[city1][city2]
               for city1, city2 in zip(tsp_path[:-1], tsp_path[1:]))


def random_cities(num_cities=100):
    '''
    create graph for Travelling Salesman
    Problem with n cities randomly distributed on
    square [0, 1) x [0, 1)
    '''
    x = [random() for _ in range(num_cities)]
    y = [random() for _ in range(num_cities)]
    cities = list(zip(x, y))

    return cities
