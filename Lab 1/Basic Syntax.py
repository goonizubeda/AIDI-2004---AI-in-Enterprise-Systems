# Python Program to calculate the square root

def square_root(number):
    # Initial guess for the square root
    guess = number / 2
    # Loop until desired precision is reached
    while True:
        # Improve the guess using the Newton's method
        new_guess = (guess + number / guess) / 2
        # Check if the guess has converged
        if abs(guess - new_guess) < 0.0001:
            break
        guess = new_guess
    return new_guess

# Take the input from the user
number = float(input('Enter a number: '))

# Calculate the square root
result = square_root(number)

# Print the result
print('The square root of {} is {}'.format(number, result))
