import math

def compute_area(base: float, height: float) -> float:
    return 0.5 * base * height

def compute_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3

# checking the value of __name__
print(__name__)

if __name__=='__main__':
    print("__name__='__main__'")
    print(compute_area(5, 3))
    print(compute_perimeter(5, 3, 4))