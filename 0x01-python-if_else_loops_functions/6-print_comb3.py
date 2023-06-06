#!/usr/bin/python3
# 6-print_comb3.py

"""Prints all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for combo1 in range(0, 10):
    for combo2 in range(combo1 + 1, 10):
        if combo1 == 8 and combo2 == 9:
            print("{}{}".format(combo1, combo2))
        else:
            print("{}{}".format(combo1, combo2), end=", ")
