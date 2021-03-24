"""
Honors Geometry
Triangle Solver Skeleton (v.1.0) 3.22.2020
"""

######  TOOLS ######

## IMPORT LIBRARIES/MODULES ##
# math module to use python's trig functions
import math

## FUNCTIONS ##
# python's trig functions use radian measure instead of degree measure,
# the following four functions just make trig work in degrees.

def Cos(degreeAngle):
    """
    Calculates the cosine of an angle in degrees
    parameters: angle in degrees (float)
    return: cosine of the angle (float)
    """
    ratio = math.cos(math.radians(degreeAngle))
    return ratio


def Sin(degreeAngle):
    """
    Calculates the sine of an angle in degrees
    parameters: angle in degrees (float)
    return: sine of the angle (float)
    """
    ratio = math.sin(math.radians(degreeAngle))
    return ratio


def InverseCos(ratio):
    """
    Calculates the degree angle measure given a ratio using cosine
    parameters: ratio (float)
    return: angle in degrees (float)
    """
    angle = math.degrees(math.acos(ratio))
    return angle


def InverseSin(ratio):
    """
    Calculates the degree angle measure given a ratio using sine
    parameters: ratio (float)
    return: angle in degrees (float)
    """
    angle = math.degrees(math.asin(ratio))
    return angle


def SSS(a, b, c):
    """
    Calculates all angles in valid SSS scenarios
    parameters: a = side, b = side, c = side
    return: list with the six triangle parts
    """
    # use law of Cosines to find angle A
    A = InverseCos((a * a - b * b - c * c)/(-1 * 2 * b * c))
    # use law of Cosines to find angle B
    B = InverseCos((b * b - a * a - c * c)/(-1 * 2 * a * c))
    # use sum of triangle angles is 180 to find C
    C = 180 - A - B
    # return all six pieces of triangle information as a list
    return [a, b, c, A, B, C]


def ASA(A, c, B):
    """
    Calculates missing angles and sides in valid ASA scenarios
    parameters: A = angle, c = side, B = Angle
    return: list with the six triangle parts
    """
    # use sum of triangle angles is 180 to find C
    C = 180 - A - B
    # use Law of Sines to find b
    b = c * Sin(B) /  Sin(C)
    # use Law of Sines to find a
    a = c * Sin(A) / Sin(C)
    # return all six pieces of triangle information as a list
    return [a, b, c, A, B, C]


def AAS(A, B, a):
    """
    Calculates missing angles and sides in valid AAS scenarios
    parameters: A = angle, B = angle, a = side
    return: list with the six triangle parts
    """
    C = 180 - A - B
    # Once we have the final angle, we have the information needed for ASA
    x = ASA(B, a, C)
    # We can take the first two elements returned from the ASA function because a in AAS is c in ASA
    return [a, x[0], x[1], A, B, C]


# TODO: write a SAS function below.
def SAS(a, C, b):
    """
    Calculates missing angles and sides in valid ASA scenarios
    parameters: a = side, C = anfle, b = side
    return: list with the six triangle parts
    """
    # Use law of cosines to solve for side c
    c = (a ** 2 + b ** 2 - 2 * a * b * Cos(C)) ** (1/2)
    # Now that we have all the sides, we can use SSS to solve for the final two angles
    x = SSS(a, b, c)
    # Use angles A and B from SSS calculation
    return [a, b, c, A, x[3], x[4]]


# TODO: write a SSA function below.
def SSA(a, b, A):
    """
    Calculates missing angles and sides in valid SSA scenarios
    parameters: a = side, b = side, A = Angle
    return: list with the six triangle parts
    """
    # do some lines of math
    return [a, b, c, A, B, C]


def Welcome():
    """
    Prints welcome message and a menu of options
    parameters: none
    return: none
    """
    print("""
This program solves triangles!
Based on specific information provided by the user about a triangle,
this program reports all sides & angles for the triangle or reports why the triangle cannot be solved.
Note: for the SSA scenario, the program reports when two triangles are possible but does not solve both triangles.

Consider a triangle ABC with sides and angles denoted in the typical way.
What triangle information do you have?
 (1) SSS
 (2) SAS
 (3) ASA
 (4) AAS
 (5) SSA""")


def UserChoice(): #TODO: Add comments to explain important parts of the "UserChoice" function
    """
    Gets a valid choice from the user from a list of triangle scenarios
    parameters: none
    return: a response from the list of numerical choices (str)
    """
    ValidChoice = False
    while ValidChoice == False:
        UserInput = input("Select an option 1 through 5: ")
        if UserInput == "1" or UserInput == "2" or UserInput == "3" or UserInput == "4" or UserInput == "5":
            ValidChoice = True
        else:
            print("Please enter a number 1 through 5! Try again.")
    return UserInput


def GetInput(sideAngle, ABC):
    return(float(input("enter " + sideAngle + " " + ABC + ": ")))


def SolveTriangle(UserInput): #TODO: Add comments to explain important parts of the "SolveTriangle" function
    """
    Based on user's choice, returns a message with triangle information OR an error message
    parameters: UserChoice (str)
    return: all sides and angles (list) or error message (str)
    """
    if UserInput == "1":
        print("You chose SSS")
        a = GetInput("side", "a")
        b = GetInput("side", "b")
        c = GetInput("side", "c")
        if a <= 0 or b <= 0 or c <= 0:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        elif a + b <= c or a + c <= b or b + c <= a:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        else:
            TriangleInfo = SSS(a, b, c)

    elif UserInput == "2":
        print("You chose SAS")
        TriangleInfo = "Student needs to write SAS function and implement it."

    elif UserInput == "3":
        print("You chose ASA")
        A = GetInput("angle", "A")
        c = GetInput("side", "c")
        B = GetInput("angle", "B")
        if c <= 0:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        elif A <= 0 or B <= 0 or A + B >=180:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        else:
            TriangleInfo = ASA(A, c, B)

    elif UserInput == "4":
        print("You chose AAS")
        A = GetInput("angle", "A")
        B = GetInput("angle", "B")
        a = GetInput("side", "a")
        if a <= 0:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        elif A <= 0 or B <= 0 or A + B >=180:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        else:
            TriangleInfo = AAS(A, B, a)

    elif UserInput == "5": #TODO write SSA function, implement it and call it.
        print("You chose SSA")
        a = GetInput("angle", "a")
        b = GetInput("side", "b")
        A = GetInput("angle", "A")
        if a <= 0 or b <= 0:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        elif A <= 0:
            TriangleInfo = "No triangle: Student needs to write appropriate error message."
        else:
            TriangleInfo = SSA(a, b, A)
        TriangleInfo = "Option 5 not yet completed."

    return TriangleInfo


# TODO write a result function here
def Results(TriangleSummary):
    return


######  MAIN PROGRAM ######

# Program summary & a menu of options (triangle cases)
Welcome()

## INPUTS ##
#Get a triangle case from the user
selectedChoice = UserChoice()

## CALCULATIONS ##
# get the triangle information based on user choice & then save triangle outcome (values or error) as variable
TriangleSummary = SolveTriangle(selectedChoice)

## OUTPUTS ##
# this print statement just checks to see that the program is getting
# to this line and that the contents of TriangleSummary are what you expect.
# this line (below) should NOT be in your final code. It should be replaced by
# a call to your Results function.
print(TriangleSummary)   #TODO replace this print statement with a call to your Results function
