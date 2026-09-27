import math

import circle

def test_circle_area_8():
    #setup
    radius = 8
    expected_area = (radius ** 2)* math.pi

    #invoke 
    actual_area = circle.circle_area(radius)

    #analyze
    assert actual_area == expected_area
