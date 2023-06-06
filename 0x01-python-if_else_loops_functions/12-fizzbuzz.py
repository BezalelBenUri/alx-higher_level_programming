#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    for nm in range(1, 101):
        if nm % 3 == 0 and nm % 5 == 0:
            print("FizzBuzz ", end="")
        elif nm % 3 == 0:
            print("Fizz ", end="")
        elif nm % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(nm), end="")
