# Ria T., Honors Geometry, 1/21/21
# My First Function
# Writing a funtion

def distance(pX, pY, qX, qY):
    """
    Find the distance between two points: (pX, pY) and (qX, qY)
    parameters: x and y coordinates of two points (float)
    return: distance between two points (float)
    """
    dist = ((qY - pY)**2 + (qX - pX)**2)**(1/2)
    return dist
