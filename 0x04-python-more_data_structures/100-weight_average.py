#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    cal = 0
    alp = 0

    for tup in my_list:
        cal += tup[0] * tup[1]
        alp += tup[1]

    return (cal / alp)
