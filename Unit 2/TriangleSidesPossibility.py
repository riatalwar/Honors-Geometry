# Have the user enter in 3 lengths for the sides of a triangle. Check to see if the triangle is possible.
# If it is, tell them a triangle is possible.
# If not, tell them how much longer the shortest leg would need to be to make it possible.

def is_possible(sides):
    longest = max(sides)
    sumOfShorter = sum(sides.remove(longest))
    return longest < sumOfShorter

def determine_change(sides):
    if is_possible(sides):
        return 'This triangle is possible.'
    else:
        longest = max(sides)
        sumOfShorter = sum(sides.remove(longest))
        changeNecessary = longest - sumOfShorter
        return 'The shortest side must be increased in length by more than ' + str(changeNecessary) + ' units.'

def run():
    sides = [int(input('Enter a side length: ')) for i in range(3)]
    print(determine_change(sides))

def test_is_possible():
    print(is_possible([1, 3, 3]) == True)
    print(is_possible([5, 4, 7]) == True)
    print(is_possible([1, 2, 3]) == False)
    print(is_possible([0, 3, 3]) == False)
    print(is_possible([1, 4, 9]) == False)

def test_determine_change():
    print(determine_change([1, 3, 3]) == 'This triangle is possible.')
    print(determine_change([0, 3, 3]) == 'The shortest side must be increased in length by more than 0 units.')
    print(determine_change([1, 4, 9]) == 'The shortest side must be increased in length by more than 4 units.')

def test():
    test_is_possible()
    test_determine_change()
