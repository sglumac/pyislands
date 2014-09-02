'''
Module contains permutation crossovers. Crossover is function
with signature:

    def crossover(penalty_function, parent1, parent2):
        ...
        return children

where object children is list of individuals.
'''
import pyislands.permutation.crossover.pmx
import pyislands.permutation.crossover.cx
import pyislands.permutation.crossover.ox1
