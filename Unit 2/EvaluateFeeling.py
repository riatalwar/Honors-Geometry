# Ria T., Honors Geometry, 9/26/20
# Evaluate Feeling
# Practice with Boolean variables and logical operators

tired = input('Are you feeling tired today? ').lower()[0]
if tired == 'y':
    print('Maybe you should try getting some more sleep.')
elif tired != 'n':
    print("That's not a valid input!")
else:
    print('You have some excellent sleep habits!')
print('Have a wonderful day!')
