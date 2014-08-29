def check_mutation(mutation):
    ''' This function asserts containing elements in permutation mutation '''
    genotype = range(10)

    new_genotype = mutation(genotype)

    for i in genotype:
        assert i in new_genotype


import tests.permutation.mutation.testrsm
import tests.permutation.mutation.testecm
