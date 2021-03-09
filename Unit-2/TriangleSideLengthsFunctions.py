"""
STUDENT NAME, Honors Geometry, 3-8-2021
Program: Triangle Side Lengths
This program will prompt the user to enter the coordinates of the vertices of a triangle.  It will then calculate and display the lengths of the sides of the triangle
"""

## FUNCTIONS ##
def WelcomeMessage ():
    """
    Print a welcome message
    parameters: none
    return: none
    """
    print("This program will prompt the user to enter the coordinates of the vertices of a triangle ABC.")
    print("It will then calculate and display the lengths of the sides of the triangle.")
    print("Warning: does not check whether the three points actually form a triangle.")

def GetPoint (pointName):
    """
    Get the x and y coordinates for a point
    parameters: name of the point (string)
    return: xCoord and yCoord of point (float)
    """
    xCoord = float(input("x-coordinate of " + pointName + ": "))
    yCoord = float(input("y-coordinate of " + pointName + ": "))
    return [xCoord, yCoord]

def Distance (Px,Py,Qx,Qy):
    """
    Calculate the distance between two points
    parameters: x and y coordinates for points P and Q (float)
    return: distance between P and Q (float)
    """
    dist = ((Qy - Py)**2 + (Qx - Px)**2)**(1/2)
    return dist

def OutputMessage(fromWhere,toWhere,dist):
    """
    Print the output message: distance between points
    parameters: the two points and distance between them (float)
    return: none
    """
    print ("The distance between points " + fromWhere + " and " + toWhere + " is: "+str(round(dist,2)))


########### MAIN PROGRAM ###########

#Program Summary
WelcomeMessage()

## INPUTS ##

#get 3 points from the user
#first Point
firstPoint = GetPoint("A")
xa = firstPoint[0]
ya = firstPoint[1]
#second Point
secondPoint = GetPoint("B")
xb = secondPoint[0]
yb = secondPoint[1]
#third Point
thirdPoint = GetPoint("C")
xc = thirdPoint[0]
yc = thirdPoint[1]

## CALCULATIONS ##

#find the distance between each pare of points
AB = Distance(xa,ya,xb,yb)
BC = Distance(xb,yb,xc,yc)
AC = Distance(xa,ya,xc,yc)

## OUTPUTS ##

#print the results
OutputMessage("A","B",AB)
OutputMessage("B","C",BC)
OutputMessage("A","C",AC)
