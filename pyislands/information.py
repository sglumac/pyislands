# coding: utf-8

__cant_touch_this = TypeError('Information should not be mutated')

class Information(dict):
    '''
    Class used for passing information from one iteration/generation
    to another iteration/generation of a genetic algorithm. This
    class should be IMMUTABLE and not changed in any part of the
    program.
    '''
    def __setitem__(self, key, value):
        ''' Don't set any items in the dictionary! '''
        raise __cant_touch_this

    def __getattr__(self, name):
        '''
        This dictionary items can be accessed as though they
        were object attributes.
        '''
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        ''' Don't set any items in the dictionary! '''
        raise __cant_touch_this
