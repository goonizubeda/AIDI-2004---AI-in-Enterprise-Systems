# Another method of calculating square root of a number.
import math
def square_root(number):
    return math.sqrt(number)

# Take the input from the user
number = float(input('Enter a number: '))

# Calculate the square root
result = square_root(float(number))

# Print the result
print('The square root of {} is {}'.format(number, result))