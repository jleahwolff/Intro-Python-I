# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

x = 4

def is_even(x):
    if x % 2 is 0:
        return print(f'{x} is Even')
    else:
        return print('Odd')

# Read a number from the keyboard
num = input('Enter a number:')
num = int(num)

print (is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_odd(number):
    if number % 2 is 0:
        print("Even!")
    else:
        print("Odd")