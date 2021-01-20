# Have the user enter in 3 lengths for the sides of a triangle. Check to see if the triangle is possible.
# If it is, tell them a triangle is possible.
# If not, tell them how much longer the shortest leg would need to be to make it possible.

def is_possible(sides):
    longest = max(sides)
    sumOfShorter = sum(sides.remove(longest))
    return longest < sumOfShorter

def determine_change(sides):
    isPossible = is_possible(sides)
    if isPossible:
        return 'This triangle is possible.'
    else:
        longest = max(sides)
        sumOfShorter = sum(sides.remove(longest))
        changeNecessary = longest - sumOfShorter
        return 'The shortest side must be increased in length by at least ' + changeNecessary + 'units.'

def run():
    sides = [int(input('Enter a side length: ')) for i in range(3)]
    print(determine_change(sides))
