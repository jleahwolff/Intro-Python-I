"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the list [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

  #create an empty list
new_list = []
new_list.append(str(y))
print(new_list)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [n**3 for n in y]

print(squares)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

ups = [word.upper() for word in a]

print(ups)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y=[num for num in x if int(num) % 2 == 0]

print(y)