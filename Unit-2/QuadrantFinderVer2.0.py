# INPUT
x = float(input("Enter the x-coordinate of a point: "))
y = float(input("Enter the y-coordinate of a point: "))

# PROCESSING
pointAsStr = "(" + str(x) + ", " + str(y) + ")"
above_Xaxis = y > 0
right_of_Yaxis = x > 0
in_Q1 = above_Xaxis and right_of_Yaxis
in_Q2 = above_Xaxis and not right_of_Yaxis
in_Q3 = not above_Xaxis and not right_of_Yaxis
in_Q4 = not above_Xaxis and right_of_Yaxis

# OUTPUT
if in_Q1:
    print("The point " + pointAsStr + " is in quadrant I")
elif in_Q2:
    print("The point " + pointAsStr + " is in quadrant II")
elif in_Q3:
    print("The point " + pointAsStr + " is in quadrant III")
else:
    print("The point " + pointAsStr + " is in quadrant IV")
