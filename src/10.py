# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE



def is_even(num):
    if num % 2 is 0:
        print(True)
        
    else:
        print(False)

# Read a number from the keyboard
num = input('Enter a number: ')
# num = int(num)

print (is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_odd(num2):
    if num2 % 2 is 0:
        print("Even!")
    else:
        print("Odd")

print(is_odd(num))