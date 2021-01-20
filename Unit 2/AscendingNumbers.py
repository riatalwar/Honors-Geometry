# Ria T., Honors Geometry, 9/26/20
# Ascending Numbers
# Sort 3 numbers into ascending order


def sort(numbers):
    if numbers[0] < numbers[1] and numbers[0] < numbers[2]:
        if numbers[1] < numbers[2]:
            return [numbers[0], numbers[1], numbers[2]]
        else:
            return [numbers[0], numbers[2], numbers[1]]
    elif numbers[1] < numbers[0] and numbers[1] < numbers[2]:
        if numbers[0] < numbers[2]:
            return [numbers[1], numbers[0], numbers[2]]
        else:
            return [numbers[1], numbers[2], numbers[1]]
    else:
        if numbers[0] < numbers[1]:
            return [numbers[2], numbers[0], numbers[1]]
        else:
            return [numbers[2], numbers[1], numbers[0]]
