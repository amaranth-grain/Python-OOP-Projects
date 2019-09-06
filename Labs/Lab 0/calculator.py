"""Demonstrates basics of Python functions."""

def sum(a, b):
    """
    Return sum of two ints.
    :param a: int
    :param b: int
    :return: sum as an int
    """
    return a + b

def multiply(a, b):
    """
    Return product of two ints.
    :param a: int
    :param b: int
    :return: product as an int
    """
    return a * b

def divide(a, b):
    """
    Return quotient of two ints.
    :param a: dividend as int
    :param b: divisor as int
    :return: quotient as an int
    """
    return a / b

def subtract(a, b):
    """
    Return difference of two ints.
    :param a: int
    :param b: int
    :return: difference as an int
    """
    return a - b

def main():
    """
    Print test results of calculator functions.
    :return: sum, product, quotient, and difference of 10 and 5
    """
    print(sum(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))
    print(subtract(10, 5))

if __name__ == "__main__":
    main()