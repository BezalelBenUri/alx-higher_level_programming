#!/usr/bin/python3
''' Module: 0-lookup
    Contains a function that returns the list of available attributes and methods of an object.
'''


def lookup(obj):
    ''' Function: lookup()
        Returns a list object containing the available attributes and methods of the given object.
    '''
    return dir(obj)
