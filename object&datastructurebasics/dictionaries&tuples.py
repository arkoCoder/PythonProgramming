# Dictionaries are unordered mappings for storing objects.This are key-value pairing which allows
# to quickly grab objects without needing to index location
# Dictionaries cannot be sorted

my_dictionary = {'k1': 1, 'k2': 'Gopal'}
print(my_dictionary['k1'])
my_dict = {'k1': [0, 1, 2], 'k2': {'kI': 'InsideKey'}}
print(my_dict['k2']['kI'])
print(my_dict['k1'][0])
my_dict['k3'] = 1.0

# Tuples are very similar to list but are immutable meaning once an element is inside a tuple it cannot be changed
# Tuples use parenthesis
# Slicing and indexing both are supported

my_tuple = (1, 1, 3)
print(type(my_tuple))
print(my_tuple.count(1))
# my_tuple[0] = 1 not possible as tuples are immutable

