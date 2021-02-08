# Ria T., Honors Geometry, 9/28/20
# Programming Assignment 0: Triangle Sides
# Calculating the side lengths of a triangle

print('Program Summary: This program will prompt the user to enter the coordinates \
    of the verticies of a triangle ABC.\nIt will then calculate and display the lengths of the sides of the triangle. \
    \nWarning: does not check whether the three points actually form a triange.')
# INPUTS
# get the x and y coordinates for each point
ax = float(input('x-coordinate of A: '))
ay = float(input('y-coordinate of A: '))
bx = float(input('x-coordinate of B: '))
by = float(input('y-coordinate of B: '))
cx = float(input('x-coordinate of C: '))
cy = float(input('y-coordinate of C: '))

# CALCULATIONS
# function to calculate distance
def calculate_distance(x1, y1, x2, y2):
    ''' calculate_distance(x1, y1, x2, y2) -> the length
    of the line segment between (x1, y1) and (x2, y2) '''
    d = ((x1 - x2)**2 + (y1 - y2)**2) ** (1/2)  # calculate distance
    return round(d, 2)  # round distance to the hundreth

def calculate_slope(x1, y1, x2, y2):
    ''' calculate_slope() -> the slope
    of the line segment between (x1, y1) and (x2, y2) '''
    return (y2 - y1)/(x2 - x1)

# OUTPUTS
# if the slopes are the same the coordinates don't form a triangle
if calculate_slope(ax, ay, bx, by) == calculate_slope(bx, by, cx, cy):
    input('The coordinates you entered do not form a triangle. Press ENTER to exit the program.')
    quit()  # quits program when user hits enter
# printing lengths
print('The lengths of the sides of the triangle are:')
print('AB =', calculate_distance(ax, ay, bx, by))
print('BC =', calculate_distance(cx, cy, bx, by))
print('AC =', calculate_distance(ax, ay, cx, cy))

#input()
