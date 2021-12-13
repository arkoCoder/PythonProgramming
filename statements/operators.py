for num in range(0, 10, 2):
    print(num)

my_string = 'Gopal'
for letter in enumerate(my_string):
    print(letter)

for index, letter in enumerate(my_string):
    print(f"Letter {letter} is present at index {index}")

# zip is used to map list items at the same indexes in tuples
my_list = [1, 2, 3]
my_list_2 = ['a', 'b', 'c']

for item in zip(my_list, my_list_2):
    print(item)

my_list_operators = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(my_list_operators))
print(max(my_list_operators))

from random import shuffle

my_list_to_shuffle = [1, 2, 3, 4]
shuffle(my_list_to_shuffle)
print(my_list_to_shuffle)

from random import randint

mynum = randint(0, 100)
print(mynum)

print([x for x in range(0, 51) if x % 3 == 0])  # comphrensions
name = input("Enter your name: ")  # input always accepts input as string
print(name)
