# List are ordered sequences that can hold a variety of object types
# They use [] brackets and commas to separate the objects in list
# It supports indexing and slicing

my_list = [1, 2, 2, "Gopal"]
another_list = ["Heda", 3]
print(my_list)
print(my_list[3])
print(my_list[1:3:1])
print(my_list + another_list)
my_list[3] = "GOPAL"  # Changing elements in the list is possible unlike STRINGS
print(my_list)
my_list.append(5)  # Adding element at end of list
print(my_list)
my_list.pop()  # Removes element from end of list
print(my_list)
my_list.pop(3)  # Removes element from passed index of list
print(my_list)
sort_list = ['a', 'z', 'b']
sort_list.sort()  # sort function doesnt return anything. Also when a function doesnt return anything is return object of type None
print(sort_list)
sort_list.reverse()  # inplace function
print(sort_list)

# Sets are unordered collections of unique elements
my_set = set()
my_set.add(1)
my_set.add(1)
print(my_set)
my_cast_list = [1, 1, 1, 1, 1, 2, 2, 2, 3]
print(set(my_cast_list))  # Casting list to set

# Booleans are "True" and "False"
b = None  # Creating a placeholder for b
print(set([1, 11, 1, 1]))

# Flattening the list
my_list_comprehension = [x for x in 'GOPAL']
print(my_list_comprehension)

my_list_comprehension1 = [num ** 2 for num in range(0, 10)]
print(my_list_comprehension1)

my_list_comprehension2 = [num ** 2 for num in range(0, 10) if num % 2 == 0]
print(my_list_comprehension2)

my_list_comprehension3 = [num if num % 2 == 0 else 'ODD' for num in range(0, 11)]
print(my_list_comprehension3)
