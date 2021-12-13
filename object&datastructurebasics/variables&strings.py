# Rules for variables in pythons:
# Names cannot start with a number
# There can be no spaces in the name, use _ instead
# Can use any of these symbols: :"',<>/?|\()!@#$%^&*~-+
# Best practice is that names should be lowercase
# Reserved words cannot be used as names eg: str, list
# Python uses DYNAMIC TYPING which means we can reassign variables to different data types
a = 2
print(a)
a = "Gopal"
print(a)
a = a + a
print(a)
a = 1
print(type(a))

# Strings are the ordered sequences of characters, using the syntax of either single or double quotes
# We can use indexing and slicing to grab sub-sections of the string
# Indexing notation uses [] notation after the string.It allows you to grab the single character from string
# Indexing starts with 0. We also have the reverse indexing for the string in python
# Slicing allows you to grab the subsection of multiple characters, a "slice" of the string
# [start:stop:step] is the syntax where start is the index for slice start, stop is the index you will go upto(but not include) and step is the size of the jump

print('hello')
print("world")
print("hello\tworld")
print(len("GOPAL HEDA"))
my_string_indexing = "Hello World"
print(my_string_indexing[6])  # Indexing example
print(my_string_indexing[-2])  # ReverseIndexing example
my_string_slicing = "abcdef"
print(my_string_slicing[2:])
print(my_string_slicing[:2])
print(my_string_slicing[2:5])
print(my_string_slicing[2:5:2])
print(my_string_slicing[::2])
print(my_string_slicing[::-1])  # Reverse the string
print("GOPAL"[2])

# Strings are immutable
# Concatenation is performed using '+'
#
name = "Gopal Heda"
# name[0] = 'H' not supported as this string is immutable
letter = 'z'
print(letter * 10)
print(letter.capitalize())
print(name.split('a'))
print(f"Hello my name is {name}")  # FStrings example
print("Hello World from {}".format("ICHALKARANJI"))
print("{1} {2} {0}".format("HEDA", "GOPAL", "ANIL"))
print('{fname} {mname} {lname}'.format(lname="HEDA", fname="GOPAL", mname="ANIL"))
