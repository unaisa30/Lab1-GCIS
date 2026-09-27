import math

def circle_area(radius):
    """ function returns the area of a circle given its radius
    """
    area = math.pi * radius ** 2
    return area

def circle_circumference(radius):
    """ function returns the circumference of a circle given its radius
    """
    circumference = 2 * math.pi * radius
    return circumference

def main():
    print("the area of a circle with radius 5 is:", circle_area(5))
    print("the circumference of a circle with radius 5 is:", circle_circumference(5))

main()
