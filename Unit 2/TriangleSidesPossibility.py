# Ria T., Honors Geometry, 1/20/21
# Determine Triangle Possibility
# Use user input for the sides of a triangle and determine
# if said triangle is possible or the change necessary if not.

def is_possible(sides):
    '''is_possible -> whether a
    triangle is possible'''
    longest = max(sides)
    sumOfShorter = sum(sides) - longest
    return longest < sumOfShorter

def determine_change(sides):
    '''determine_change() -> determine if change
    is necessary and the amount of change'''
    if is_possible(sides):
        return 'This triangle is possible.'
    else:   # if triangle not possible determine amount of necessary change
        longest = max(sides)
        sumOfShorter = sum(sides) - longest
        changeNecessary = longest - sumOfShorter
        return 'The shortest side must be increased in length by more than ' + str(changeNecessary) + ' units.'

def run():
    '''run() -> get user input and print results'''
    sides = [int(input('Enter a side length: ')) for i in range(3)]
    print(determine_change(sides))

def test_is_possible():
    '''test_is_possible() -> test cases
    for the funtion is_possible()'''
    print(is_possible([1, 3, 3]) == True)
    print(is_possible([5, 4, 7]) == True)
    print(is_possible([1, 2, 3]) == False)
    print(is_possible([0, 3, 3]) == False)
    print(is_possible([1, 4, 9]) == False)

def test_determine_change():
    '''test_determine_change() -> test cases
    for the funtion determine_change()'''
    print(determine_change([1, 3, 3]) == 'This triangle is possible.')
    print(determine_change([0, 3, 3]) == 'The shortest side must be increased in length by more than 0 units.')
    print(determine_change([1, 4, 9]) == 'The shortest side must be increased in length by more than 4 units.')

def test():
    '''test() -> run test code from
    test_is_possible() and test_determine_change()'''
    test_is_possible()
    test_determine_change()

test()
