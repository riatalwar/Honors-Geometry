# Ria T., Honors Geometry, 5/7/2021
# Triangle Solver
# Determine the missing angles and sides of a triangle

######  TOOLS ######

## IMPORT LIBRARIES/MODULES ##
import math
import turtle

## FUNCTIONS ##

# Trig functions
def Cos(degreeAngle):
    """
    Calculates the cosine of an angle in degrees
    parameters: angle in degrees (float)
    return: cosine of the angle (float)
    """
    # I modified this for efficiency so that no variable is necessary
    return math.cos(math.radians(degreeAngle))


def Sin(degreeAngle):
    """
    Calculates the sine of an angle in degrees
    parameters: angle in degrees (float)
    return: sine of the angle (float)
    """
    # I modified this for efficiency so that no variable is necessary
    return math.sin(math.radians(degreeAngle))


def InverseCos(ratio):
    """
    Calculates the degree angle measure given a ratio using cosine
    parameters: ratio (float)
    return: angle in degrees (float)
    """
    # I modified this for efficiency so that no variable is necessary
    return math.degrees(math.acos(ratio))


def InverseSin(ratio):
    """
    Calculates the degree angle measure given a ratio using sine
    parameters: ratio (float)
    return: angle in degrees (float)
    """
    # I modified this for efficiency so that no variable is necessary
    return math.degrees(math.asin(ratio))


# Triangle solver functions
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


def SAS(a, C, b):
    """
    Calculates missing angles and sides in valid ASA scenarios
    parameters: a = side, C = angle, b = side
    return: list with the six triangle parts
    """
    # Use law of cosines to solve for side c
    c = (a ** 2 + b ** 2 - 2 * a * b * Cos(C)) ** (1/2)
    # Now that we have all the sides, we can use SSS to solve for the final two angles
    x = SSS(a, b, c)
    # Use angles A and B from SSS calculation
    return [a, b, c, x[3], x[4], C]


def SSA(a, b, A, ambiguous=False):
    """
    Calculates missing angles and sides in valid SSA scenarios
    parameters: a = side, b = side, A = Angle
    return: list with the six triangle parts
    """
    # Use law of sines to get angle B
    B = InverseSin(b * Sin(A) / a)
    # Now we have all the information necessary for AAS
    x = AAS(A, B, a)
    # Calculates a second triangle if ambiguous
    if ambiguous:
        B2 = 180 - B
        C2 = 180 - A - B2
        # Use sides and angles to calculate the final side using law of cosines
        c2 = (a ** 2 + b ** 2 - 2 * a * b * Cos(C2)) ** (1/2)
        # Return both cases
        return [[a, b, x[2], A, B, x[5]], [a, b, c2, A, B2, C2]]

    # Return one case if not ambiguous
    return [a, b, x[2], A, B, x[5]]


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


def UserChoice():
    """
    Gets a valid choice from the user from a list of triangle scenarios
    parameters: none
    return: a response from the list of numerical choices (str)
    """
    # I modified the original code to make it more efficient
    # This way, there is no need to have a variable tracking the validity
    while True:
        userInput = input("Select an option 1 through 5: ") # Get user input
        if userInput in ['1', '2', '3', '4', '5']:
            return userInput                                # If input is from 1 - 5 then it is valid and can be returned
        # If invalid print error message and repeat
        print("Please enter a number 1 through 5! Try again.")


def GetInput(sideAngle, ABC):
    return(float(input("Enter " + sideAngle + " " + ABC + ": ")))


def GetSidesAngles(userInput):
    """
    Get the sides and angles from the user
    parameters: userInput (string)
    return: sides and angles (list)
    """
    if userInput == "1":
        sidesAngles = (("side", "a"), ("side", "b"), ("side", "c"))
    elif userInput == "2":
        sidesAngles = (("side", "a"), ("angle", "C"), ("side", "b"))
    elif userInput == "3":
        sidesAngles = (("angle", "A"), ("side", "c"), ("angle", "B"))
    elif userInput == "4":
        sidesAngles = (("angle", "A"), ("angle", "B"), ("side", "a"))
    elif userInput == "5":
        sidesAngles = (("side", "a"), ("side", "b"), ("angle", "A"))
    return [GetInput(sidesAngles[i][0], sidesAngles[i][1]) for i in range(3)]


def SolveTriangle(userInput):
    """
    Based on user's choice, returns a message with triangle information OR an error message
    parameters: UserChoice (str)
    return: all sides and angles (list) or error message (str)
    """
    # I modified this function for efficiency
    # This way, the else clause is eliminated and there is one less variable needed
    if userInput == "1":
        print("You chose SSS")
        # Get sides
        a, b, c = GetSidesAngles(userInput)
        # Check if sides are valid
        if a <= 0 or b <= 0 or c <= 0:
            return "No triangle: one or more given sides are 0 or negative."
        elif a + b <= c or a + c <= b or b + c <= a:
            return "No triangle: triangle inequality is not satisfied."
        return SSS(a, b, c)

    elif userInput == "2":
        print("You chose SAS")
        # Get sides and angles
        a, C, b = GetSidesAngles(userInput)
        # Check if sides are valid
        if a <= 0 or b <= 0:
            return "No triangle: one or more given sides are 0 or negative."
        # Check if angle is valid
        elif C <= 0 or C >= 180:
            return "No triangle: one or more given angles are too small or too big."
        return SAS(a, C, b)

    elif userInput == "3":
        print("You chose ASA")
        # Get sides and angles
        A, c, B = GetSidesAngles(userInput)
        # Check if side is valid
        if c <= 0:
            return "No triangle: one or more given sides are 0 or negative."
        # Check is angles are valid
        elif A <= 0 or B <= 0 or A + B >= 180:
            return "No triangle: one or more given angles are too small or too big."
        return ASA(A, c, B)

    elif userInput == "4":
        print("You chose AAS")
        # Get sides and angles
        A, B, a = GetSidesAngles(userInput)
        # Check is side is valid
        if a <= 0:
            return "No triangle: one or more given sides are 0 or negative."
        # Check is angles are valid
        elif A <= 0 or B <= 0 or A + B >= 180:
            return "No triangle: one or more given angles are too small or too big."
        return AAS(A, B, a)

    elif userInput == "5":
        print("You chose SSA")
        # Get sides and angles
        a, b, A = GetSidesAngles(userInput)
        # Calculate height of the triangle
        h = round(Sin(A) * b, 2)
        # Check if sides are valid
        if a <= 0 or b <= 0:
            return "No triangle: one or more given sides are 0 or negative."
        # Check is angle is valid
        elif A <= 0 or A >= 180:
            return "No triangle: one or more given angles are too small or too big."
        # Ensure that the triangle is possible
        elif A > 90 and a <= b:
            return "No triangle: leg a is too short with that non-acute angle A."
        elif a < h:
            return "No triangle: leg a is shorter than the altitude from C."
        elif a > h and a < b: # Ambiguous case
            return SSA(a, b, A, ambiguous=True)
        return SSA(a, b, A)


def TurtleDraw(triangleSummary):
    """
    Uses turtle to draw a triangle based on triangleSummary
    parameters: triangleSummary (list)
    return: none
    """
    wn = turtle.Screen()    # Create window
    jerry = turtle.Turtle() # Create Turtle
    angleIndex = [5, 3, 4]  # The order in which the angles are used
    for i in range(3):      # Draw each side
        jerry.forward(triangleSummary[i] * 20)
        jerry.left(180 - triangleSummary[angleIndex[i]])
    input("Press ENTER to continue.")
    wn.clear()              # Clear window


def AreaPerimeter(triangleSummary):
    """
    Prints the results of the triangle with proper formatting
    parameters: triangleSummary (list)
    return: area, perimeter (int)
    """
    area = 0.5 * triangleSummary[0] * triangleSummary[1] * Sin(triangleSummary[5])
    perimeter = triangleSummary[0] + triangleSummary[1] + triangleSummary[2]
    return area, perimeter


def Results(triangleSummary):
    """
    Prints the results of the triangle with proper formatting
    parameters: triangleSummary (string or list)
    return: none
    """
    print("Results for your triangle ABC:")
    # Prints error message is triangleSummary is a string
    if type(triangleSummary) is str:
        print(triangleSummary)
    # Prints the results with proper formatting
    else:
        print("Sides:  a = " + str(round(triangleSummary[0], 2)) + " , b = " + str(round(triangleSummary[1], 2)) +
               " , c = " + str(round(triangleSummary[2], 2)) + "\n" +
               "Angles: A = " + str(round(triangleSummary[3], 2)) + " , B = " + str(round(triangleSummary[4], 2)) +
               " , C = " + str(round(triangleSummary[5], 2)))
        TurtleDraw(triangleSummary) # Draw turtle

        if input("Do you want the area and perimeter of the triangle? ").lower()[0] == 'y':
            area, perimeter = AreaPerimeter(triangleSummary)
            print("Area:", round(area, 2), "\nPerimeter:", round(perimeter, 2))


def Play():
    """
    Runs the program
    parameters: none
    return: none
    """
    ## INPUTS ##
    # Get a triangle case from the user
    selectedChoice = UserChoice()

    ## CALCULATIONS ##
    # get the triangle information based on user choice & then save triangle outcome (values or error) as variable
    triangleSummary = SolveTriangle(selectedChoice)

    ## OUTPUTS ##
    # This prints the results of the triangle or an error message
    # The ambiguous case
    if type(triangleSummary) == list and len(triangleSummary) == 2:
        print("The Ambiguous Case:")
        Results(triangleSummary[0])
        print()
        Results(triangleSummary[1])
    else:
        Results(triangleSummary)

    # Asks user if they want to play again
    PlayAgain()


def PlayAgain():
    """
    Asks user if they want to play again
    parameters: none
    return: none
    """
    print()
    # Asks user if they want to play again and call Play() if they do
    if input("Do you want to play again? ").lower()[0] == 'y':
        print()
        Play()

######  MAIN PROGRAM ######

# Program summary & a menu of options (triangle cases)
Welcome()

Play()
