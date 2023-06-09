#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeros if smaller than 2 elements
    tuple_a += (0, 0)[:2 - len(tuple_a)]
    tuple_b += (0, 0)[:2 - len(tuple_b)]
    
    # Perform addition and return result as a tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
