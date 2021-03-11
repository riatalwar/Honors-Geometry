"""
Ria Talwar, Honors Geometry, 03-10-21
Assignment # - Quadratic Solutions
This program determines the number of real solutions to a quadratic function when set equal to 0.
"""

## PROGRAM SUMMARY
print("This program will take the coefficients of a quadratic function, in the form of ax^2 + bx +c.")
print("It will then report the number of real solutions when the quadratic function is equal to 0.")
print("Note: the program only works for non-zero 'a' values and reports the number of real solultions, not the solutions themselves.")


## FUNCTIONS
def QuadSolutions(a, b, c):
    """
    Determines the number of real solutions to a quadratic equation, ax^2+bx+c=0
    Parameters: the coefficients of the quadratic, linear, and constant terms: (floats)
    Return: message containing number of solutions: (str)
    """




######### MAIN PROGRAM #########

## INPUTS
firstVal=float(input("Type in the coefficient to the x^2 term: "))
secondVal= "###"
thirdVal= "###"

## CALCULATIONS
outputMessage = "***Student needs to write and call the function QuadSolutions.***"

## OUTPUTS
print("The quadratic equation " + str(firstVal) + "x^2 + " + str(secondVal) + "x + " + str(thirdVal) + " = 0 has " + outputMessage)
