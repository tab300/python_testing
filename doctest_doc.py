# doctest_doc.py

"""
TESTING USING doctest

"""

# A method for calculating simple interest on a given principal

def simple_interest(principal, rate, time):
    """
    >>> print(simple_interest(500, 5, 2))
    50.0

    """
    return principal * rate * time /100


# A method for calculating compound interest future value on a given principal

def fv_compound_interest(principal, rate, time):
    """
    >>> print(fv_compound_interest(500, 5, 2))
    550.0

    """
    return principal + (principal * rate * time /100)

import doctest
doctest.testmod()


