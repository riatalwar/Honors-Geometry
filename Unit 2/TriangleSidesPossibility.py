# Have the user enter in 3 lengths for the sides of a triangle. Check to see if the triangle is possible.
# If it is, tell them a triangle is possible.
# If not, tell them how much longer the shortest leg would need to be to make it possible.

def is_possible(sides):
    longest = max(sides)
    sumOfShorter = sum(sides.remove(longest))
    return longest < sumOfShorter
