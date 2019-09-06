import test

def sum(a, b):
    return a + b

def main():
    """
    Return sum of two ints.
    :return: sum as int
    """
    num1 = int(input("Enter first value: "))
    num2 = int(input("Enter second value: "))
    print(sum(num1, num2))

if __name__ == "__main__":
    print("This shows imported variables outside of __main__ conditional: " + str(test.test))
    main()

