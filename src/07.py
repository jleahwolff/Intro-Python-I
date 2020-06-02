"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
sec_el = a[1]
print(sec_el)

# Output the second-to-last element: 9
sec_to_last = a[4]
print(sec_to_last)

# Output the last three elements in the array: [7, 9, 6]
last_three = a[3:]
print(last_three)

# Output the two middle elements in the array: [1, 7]
two_mid = a[2:4]
print(two_mid)

# Output every element except the first one: [4, 1, 7, 9, 6]
all_but_zero = a[1:]
print(all_but_zero)

# Output every element except the last one: [2, 4, 1, 7, 9]
all_but_five = a[:5]
print(all_but_five)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
eigth_twelve = s[7:12]
print(eigth_twelve)