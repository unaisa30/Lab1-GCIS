import math

def middle(str1):
    """ function returns middle letters of a string (this is a docstring)
    """

    ''' this is a normal multi-line comment, it is not a docstring.
    '''
    if len(str1) % 2 == 0:
        mid1 = len(str1) // 2 - 1
        mid2 = len(str1) // 2 
        return str1[mid1:mid2 + 1]
    else:
        mid = len(str1) // 2
        return str1[mid]


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
    str1 = input("enter string you want:")
    print(middle(str1))
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    sum = num1 + num2
    print("The sum of num1 and num2 is:", sum)
    x = math.pi*num1
    print("The area of a circle with radius", num1, "is:", circle_area(num1))
main()
    



