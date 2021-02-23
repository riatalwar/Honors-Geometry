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
print("\nIs " + pointAsStr + " in quadrant I? " + str(in_Q1))
print("Is " + pointAsStr + " in quadrant II? " + str(in_Q2))
print("Is " + pointAsStr + " in quadrant III? " + str(in_Q3))
print("Is " + pointAsStr + " in quadrant IV? " + str(in_Q4))
