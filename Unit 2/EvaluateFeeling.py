# Ria T., Honors Geometry, 9/26/20
# Evaluate Feeling
# Practice with Boolean variables and logical operators

def evaluate(isTired):
    isTired = isTired.lower()[0]
    if isTired == 'y':
        return 'Maybe you should try getting some more sleep.'
    elif isTired == 'n':
        return 'You have some excellent sleep habits!'
    else:
        return "That's not a valid input!"

def run():
    isTired = input('Are you feeling tired today? ')
    print(evaluate(isTired), '\nHave a wonderful day!')

def test():
    print(evaluate('Y') == 'Maybe you should try getting some more sleep.')
    print(evaluate('yes') == 'Maybe you should try getting some more sleep.')
    print(evaluate('No') == 'You have some excellent sleep habits!')
    print(evaluate('n') == 'You have some excellent sleep habits!')
    print(evaluate('dsf') == "That's not a valid input!")

run()
