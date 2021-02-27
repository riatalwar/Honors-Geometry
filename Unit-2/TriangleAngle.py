# Ria T., Honors Geometry, 2/27/21
# Determine Triangle Angle
# Use user input for the sides of a triangle and determine whether the angle is obtuse, right, or acute

def is_possible(sides):
    '''is_possible() -> whether a
    triangle is possible'''
    sides.sort()
    longest = sides[2]
    sumOfShorter = sum(sides) - longest
    return longest < sumOfShorter

def find_angle(sides):
    '''find_angle() -> whether an
    angle is obtuse, right, or acute'''
    sides.sort()
    longestSquared = sides[2] ** 2
    legsSquared = sides[0] ** 2 + sides[1] ** 2

    if longestSquared >= legsSquared:
        return "obtuse"
    elif longestSquared == legsSquared:
        return "right"
    else:
        return "acute"

def run():
    sides = [int(input("Enter a side length: ")) for i in range(3)]
    if is_possible(sides):
        angle = find_angle(sides)
        print("The angle is a(n)", angle, "angle.")
    else:
        print("Invalid triangle")

run()
