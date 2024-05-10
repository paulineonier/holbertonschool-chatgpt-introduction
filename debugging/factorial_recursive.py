#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Computes the factorial of a given non-negative integer.

    Parameters:
    - n (int): The non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

