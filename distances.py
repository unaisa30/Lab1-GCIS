# ACTIVITY 2: Finding the distance between two points.

# Just using varibbles:

x1 = 3
y1 = 2
x2 = 7
y2 = 5

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("the distance between two points is:", distance)

# defining a function to find the distance between two points to make it reusable:

def calculate_distance(x1,x2,y1,y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

print("the distance between two points is:", calculate_distance(3,7,2,5))
print("the distance between two points is:", calculate_distance(2,4,6,8)) 
print("the distance between two points is:", calculate_distance(1,10,5,6))

# calculating distance of a line using 3 points:

def line_distance(x1,x2,x3,y1,y2,y3):
    distance1 = calculate_distance(x1,x2,y1,y2)
    distance2 = calculate_distance(x2,x3,y2,y3)
    total_distance = distance1 + distance2
    return total_distance

print("the distance of a line using 3 points is:", line_distance(2,5,9,3,8,6))



