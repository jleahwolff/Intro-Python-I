# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE

def f1(x,y):
    return x + y

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE

def f2(*num):
    sum = 0
    for n in num:
        sum = n + sum

    print(sum)

f2(2,3,4,5) #should return 14

a = [7, 6, 5, 4]

# # How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE

def f3(value1, value2):
    #if theres one argument, it returns that value +1
    if value2 != 0:
        print(value1 + value2)
    #else it returns the sum of two arguments
    else:
        print(value1 + 1)

f3(2, 4)


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**keyVal):
    for key, value in keyVal.items():
        print("{}: {}".format(key, value))

print(f4(key="Duluth", value="Minnesota"))
print(f4(key=42, value="Louisiana"))


d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)
