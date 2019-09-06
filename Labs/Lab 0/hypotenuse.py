import math

def main():
    a = int(input("Triangle side 1: "))
    b = int(input("Triangle side 2: "))
    return print("Hypotenuse is " + str(math.sqrt(a**2 + b**2)))

if __name__ == "__main__":
    main()