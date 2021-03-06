"""
Program Summary:
This program will take a list of triangle measures for triangle ABC - side lenghts (a,b,c)
followed by angle measures (A,B,C) - and display these in a user-friendly format.
"""

# NO INPUT

# PROCESSING
SideAngleMeasures = [3.6, 2.0, 5.1, 33.30240516500015, 17.76009924291366, 128.93749559208618]
for i in range(len(SideAngleMeasures)):
    SideAngleMeasures[i] = round(SideAngleMeasures[i], 2)

# OUTPUT
print("Results for your triangle ABC:")
print("a = " + str(SideAngleMeasures[0]) + ", b = " + str(SideAngleMeasures[1]) + ", c = " + str(SideAngleMeasures[2]))
print("A = " + str(SideAngleMeasures[3]) + ", B = " + str(SideAngleMeasures[4]) + ", C = " + str(SideAngleMeasures[5]))
