# Ria T., Honors Geometry, 1/20/21
# Ascending Numbers
# Sort three numbers into ascending order

def sort(numbers):
    '''sort(numbers) -> a sorted version of numbers'''
    if numbers[0] <= numbers[1] and numbers[0] <= numbers[2]:
        if numbers[1] <= numbers[2]:
            return [numbers[0], numbers[1], numbers[2]]
        else:
            return [numbers[0], numbers[2], numbers[1]]
    elif numbers[1] <= numbers[0] and numbers[1] <= numbers[2]:
        if numbers[0] <= numbers[2]:
            return [numbers[1], numbers[0], numbers[2]]
        else:
            return [numbers[1], numbers[2], numbers[1]]
    else:
        if numbers[0] <= numbers[1]:
            return [numbers[2], numbers[0], numbers[1]]
        else:
            return [numbers[2], numbers[1], numbers[0]]

def run():
    '''run() -> get list of int from
    user and print sorted list'''
    numbers = [int(input('Enter an integer: ')) for i in range(3)]
    sorted = sort(numbers)
    print(sorted[0], sorted[1], sorted[2])

def test():
    '''test() -> test cases for sort()'''
    print(sort([1, 2, 3]) == [1, 2, 3])
    print(sort([3, 2, 1]) == [1, 2, 3])
    print(sort([1, 3, 2]) == [1, 2, 3])
    print(sort([1, 1, 3]) == [1, 1, 3])
    print(sort([4, 4, 3]) == [3, 4, 4])
    print(sort([5, 8, 5]) == [5, 5, 8])

run()
