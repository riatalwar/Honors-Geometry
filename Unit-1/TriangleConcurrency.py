# Ria T., Honors Geometry, 10/8/20
# Programming Assignment 1: Triangle Concurrency
# Calculating and plotting the concurrency points of a triangle

import matplotlib.pyplot as plt

# CALCULATIONS
def calculate_circumcenter(ax, ay, bx, by, cx, cy):
    ''' calculate_circumcenter() -> circumcenter
    at point (x, y) for triangle ABC '''
    mPerpToAB = (bx - ax)/(ay - by)     # slope of a line perpendicular to AB
    mPerpToAC = (cx - ax)/(ay - cy)     # slope of a line perpendicular to AC
    # get midpoints
    midABx = (ax + bx) / 2
    midABy = (ay + by) / 2
    midACx = (ax + cx) / 2
    midACy = (ay + cy) / 2
    # calculate x and y coordinates
    x = (mPerpToAB * midABx - mPerpToAC * midACx + midACy - midABy) / (mPerpToAB - mPerpToAC)
    y = mPerpToAB * x - mPerpToAB * midABx + midABy
    return round(x, 2), round(y, 2)    # round and return coordinates

def calculate_centroid(ax, ay, bx, by, cx, cy):
    ''' calculate_centroid() -> centroid
    at point (x, y) for triangle ABC '''
    mCToAB = (2 * cy - ay - by)/(2 * cx - ax - bx) # slope going from point C to line AB
    mBToAC = (2 * by - ay - cy)/(2 * bx - ax - cx) # slope going from point B to line AC
    # calculate x and y coordinates
    x = (mCToAB * cx - mBToAC * bx + by - cy)/(mCToAB - mBToAC)
    y = mCToAB * (x - cx) + cy
    return round(x, 2), round(y, 2)    # round and return coordinates

def calculate_orthocenter(ax, ay, bx, by, cx, cy):
    ''' calculate_orthocenter() -> orthocenter
    at point (x, y) for triangle ABC '''
    mAB = (by - ay)/(bx - ax)    # slope of line AB
    mBC = (cy - by)/(cx - bx)    # slope of line BC
    mAltToAB = -1/mAB            # slope of the altitude from line AB
    mAltToBC = -1/mBC            # slope of the altitude from line BC
    # calculate x and y coordinates
    x = (mAltToAB * cx - cy - mAltToBC * ax + ay)/(mAltToAB - mAltToBC)
    y = mAltToBC * (x - ax) + ay
    return round(x, 2), round(y, 2)    # round and return coordinates

def run():
    ''' run() performs the calculations and displays the plot '''
    # print program summary
    print('Program Summary: This program will prompt the user to enter the coordinates of the vertices of a triangle ABC. \
        \nIt will then calculate the coordinates of the concurrency points and print the results.\
        \nIn addition, a plot of the triangle and the concurrency points will be displayed. \
        \nWarning: This program will not work if any median, perp. bisector, or altitude is a vertical line.')

    # INPUTS
    # get coordinates
    ax = float(input('x-coordinate of A: '))
    ay = float(input('y-coordinate of A: '))
    bx = float(input('x-coordinate of B: '))
    by = float(input('y-coordinate of B: '))
    cx = float(input('x-coordinate of C: '))
    cy = float(input('y-coordinate of C: '))

    # CALCULATIONS & OUTPUTS
    # calculate concurrency points -- see functions above for the formulas &  print points
    print('\nTriangle ABC with A =', (ax, ay), 'B =', (bx, by), 'C =', (cx, cy), 'has')
    try:
        xCirc, yCirc = calculate_circumcenter(ax, ay, bx, by, cx, cy)
        print('its circumcenter at:', (xCirc, yCirc))
    except:
        xCirc, yCirc = 1, 1
        print('its circumcenter cannot be calculated')
    try:
        xCent, yCent = calculate_centroid(ax, ay, bx, by, cx, cy)
        print('its centroid at:', (xCent, yCent))
    except:
        xCent, yCent = 1, 1
        print('its centroid cannot be calculated')
    try:
        xOrth, yOrth = calculate_orthocenter(ax, ay, bx, by, cx, cy)
        print('its orthocenter at:', (xOrth, yOrth))
    except:
        xOrth, yOrth = 1, 1
        print('its orthocenter cannot be calculated')

    # set plot size and axis
    plt.figure(figsize=(6, 6))
    plt.axis([-10, 10, -10, 10])
    plt.xticks(ticks=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks(ticks=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])

    # plot triangle and label points
    plt.plot([ax, bx, cx, ax], [ay, by, cy, ay], 'b')
    plt.plot([ax, bx, cx], [ay, by, cy], 'co')
    plt.annotate('A', (ax + 0.2, ay + 0.2))
    plt.annotate('B', (bx + 0.2, by + 0.2))
    plt.annotate('C', (cx + 0.2, cy + 0.2))

    # plot and label concurrency points
    plt.plot([xCirc, xCent, xOrth], [yCirc, yCent, yOrth], 'kD')
    plt.annotate('Circumcenter', (xCirc + 0.2, yCirc + 0.2))
    plt.annotate('Centroid', (xCent + 0.2, yCent + 0.2))
    plt.annotate('Orthocenter', (xOrth + 0.2, yOrth + 0.2))
    plt.show()

run()

def test_circumcenter():
    ''' test_circumcenter() ensures that some test cases
    for calculate_circumcenter() return accurate results '''
    print(calculate_circumcenter(-5, 6, 8, -1, -3, -2) == (2.04, 3.51))
    print(calculate_circumcenter(2, 3, 1, 7, -5, -8) == (-9.12, 2.35))
    print(calculate_circumcenter(-1, 1, 3, -4, 5, 5) == (3.61, 0.59))
    print(calculate_circumcenter(1.5, 2.21, -3, -8, 7.713, 8.21345) == (22.22, -13.02))

def test_centroid():
    ''' test_centroid() ensures that some test cases
    for calculate_centroid() return accurate results '''
    print(calculate_centroid(-5, 6, 8, -1, -3, -2) == (0.0, 1.0))
    print(calculate_centroid(2, 3, 1, 7, -5, -8) == (-0.67, 0.67))
    print(calculate_centroid(-1, 1, 3, -4, 5, 5) == (2.33, 0.67))
    print(calculate_centroid(1.5, 2.21, -3, -8, 7.713, 8.21345) == (2.07, 0.81))

def test_orthocenter():
    ''' test_orthocenter() ensures that some test cases
    for calculate_orthocenter() return accurate results '''
    print(calculate_orthocenter(-5, 6, 8, -1, -3, -2) == (-4.09, -4.02))
    print(calculate_orthocenter(2, 3, 1, 7, -5, -8) == (16.23, -2.69))
    print(calculate_orthocenter(-1, 1, 3, -4, 5, 5) == (-0.22, 0.83))
    print(calculate_orthocenter(1.5, 2.21, -3, -8, 7.713, 8.21345) == (-38.23, 28.46))

def test():
    print('Circumcenter')
    test_circumcenter()
    print('\nCentroid')
    test_centroid()
    print('\nOrthocenter')
    test_orthocenter()

#test()
