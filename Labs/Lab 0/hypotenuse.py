import math

def CalculateHypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    print(CalculateHypotenuse(3,4))

if __name__ == "__main__":
    main()