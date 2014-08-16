from math import sqrt


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


def evaluate_cycle(adjacency_matrix, tsp_cycle):
    '''
    function for evaluation of cycle given list

    tsp_cycle = [city0, city1, city2, ..., cityn-1, city0]
    '''
    return sum(adjacency_matrix[city1][city2]
               for city1, city2 in izip(tsp_cycle[:-1], tsp_cycle[1:]))
