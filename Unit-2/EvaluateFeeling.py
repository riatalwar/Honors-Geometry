# Ria T., Honors Geometry, 1/20/21
# Evaluate Feeling
# Practice with Boolean variables and logical operators

def evaluate(isTired):
    '''evaluate(isTired) -> evaluate isTired
    and return appropriate message'''
    isTired = isTired.lower()[0]    # take only a lowercase version of the first letter to evaluate
    if isTired == 'y':
        return 'Maybe you should try getting some more sleep.'
    elif isTired == 'n':
        return 'You have some excellent sleep habits!'
    else:                           # if answer is neither yes nor no
        return "That's not a valid input!"

def run():
    '''run() -> get user input and print messages'''
    isTired = input('Are you feeling tired today? ')
    print(evaluate(isTired), '\nHave a wonderful day!')

def test():
    '''test() -> test cases for evaluate()'''
    print(evaluate('Y') == 'Maybe you should try getting some more sleep.')
    print(evaluate('yes') == 'Maybe you should try getting some more sleep.')
    print(evaluate('No') == 'You have some excellent sleep habits!')
    print(evaluate('n') == 'You have some excellent sleep habits!')
    print(evaluate('dsf') == "That's not a valid input!")

run()
