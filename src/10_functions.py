# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
x = 4

def is_even(x):
    return bool(x % 2)

# Read a number from the keyboard
num = input('3')
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_odd(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")
