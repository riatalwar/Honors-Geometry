# Ria T., Honors Geometry, 9/26/20
# Ascending Numbers
# Sort 3 numbers into ascending order

numbers = [int(input('Enter an integer: ')) for i in range(3)]
if numbers[0] < numbers[1] and numbers[0] < numbers[2]:
    if numbers[1] < numbers[2]:
        sorted = [numbers[0], numbers[1], numbers[2]]
    else:
        sorted = [numbers[0], numbers[2], numbers[1]]
elif numbers[1] < numbers[0] and numbers[1] < numbers[2]:
    if numbers[0] < numbers[2]:
        sorted = [numbers[1], numbers[0], numbers[2]]
    else:
        sorted = [numbers[1], numbers[2], numbers[1]]
