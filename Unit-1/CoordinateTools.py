# Ria T., Honors Geometry, 9/25/20
# Coordinate Tools
# Building a slope, midpoint, and distance calculator

def calculate_slope(x1, y1, x2, y2):
    ''' calculate_slope() -> the slope
    of the line segment between (x1, y1) and (x2, y2) '''
    return (y2 - y1)/(x2 - x1)

def calculate_midpoint(x1, y1, x2, y2):
    ''' calculate_midpoint() -> the midpoint
    of the line segment between (x1, y1) and (x2, y2) '''
    return (x1 + x2)/2, (y1 + y2)/2

def calculate_distance(x1, y1, x2, y2):
    ''' calculate_distance() -> the length
    of the line segment between (x1, y1) and (x2, y2) '''
    return ((x1 - x2)**2 + (y1 - y2)**2) ** (1/2)

def coordinate_tools_calculator(x1, y1, x2, y2):
    ''' coordinate_tools_calculator() ->
    slope, midpoint, and distance of x1, y1, x2, y2 '''
    # gets the values
    slope = calculate_slope(x1, y1, x2, y2)
    midpoint = calculate_midpoint(x1, y1, x2, y2)
    distance = calculate_distance(x1, y1, x2, y2)
    # creates and returns a message
    message = 'The slope is ' + str(slope) + ', the midpont is (' + str(midpoint[0]) + ', ' + \
        str(midpoint[1]) + '), and the distance is ' + str(distance) + '.'
    return message

x1, y1 = [int(n) for n in input('Enter a point: ').split(', ')]
x2, y2 = [int(n) for n in input('Enter a point: ').split(', ')]
print(coordinate_tools_calculator(x1, y1, x2, y2))
