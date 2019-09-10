"""Demonstrates basics of Python functions."""

def sum(a, b):
    """
    Return sum of two ints.
    :param a: int
    :param b: int
    :return: sum as an int
    """
    return a + b

def subtract(a, b):
    """
    Return difference of two ints.
    :param a: int
    :param b: int
    :return: difference as an int
    """
    return a - b

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

def main():
    """
    Print the calculator result based on user input.
    :return: sum, product, quotient, and difference of 10 and 5
    """
    print("Select from menu:")
    print("1. Add")
    print("2. Minus")
    print("3. Multiple")
    print("4. Divide")

    choice = int(input("Enter your choice: "))
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

    input_dict = {1: sum(a, b), 2: subtract(a, b), 3: multiply(a, b), 4: divide(a, b)}
    answer_dict = {1: "sum", 2: "difference", 3: "product", 4:"quotient"}
    print("The {0} of {1} and {2} is {3}.".format(answer_dict.get(choice),
                                                 a,
                                                 b,
                                                 input_dict.get(choice, "Invalid input.  Select from menu.")))

if __name__ == "__main__":
    main()