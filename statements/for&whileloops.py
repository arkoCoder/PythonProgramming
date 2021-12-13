my_list = [1, 1, 2, 3, 5, 4]
for item_name in my_list:
    print(item_name)

my_string = "GOPAL"
for string_item in my_string:
    print(string_item)

print("FIBONACCI!!")
first_num = 0
second_num = 1
fib_sum = 0
for num in range(10):
    print(first_num)
    fib_sum = first_num + second_num
    first_num = second_num
    second_num = fib_sum

my_tup_list = [(1, 2), (3, 4)]
print("Each element of list")
for tup in my_tup_list:
    print(tup)
print("Each element of tuple i.e. TUPLE UNPACKING")
for (a, b) in my_tup_list:
    print(a)
    print(b)

print("Dictionary Iteration!")
my_dictionary = {'k1': 1, 'k2': 2}
for key, values in my_dictionary.items():  # my_dictionary.items() returns tuples hence used the tuple unpacking concept
    print(key)
    print(values)

for values in my_dictionary.values():
    print(values)

print("Starting while loop")
iterator = 0
while iterator < 5:
    print(f"Value of iterator is {iterator}")
    iterator += 1
else:
    print("Value exceeds 5")

# break: breaks out of current closest enclosing loop
# continue: Goes to the top of the closes enclosing loop
# pass: Does nothing at all

for num in range(5):
    pass  # this can be used as a placeholder for further code implementation

my_string_continue = "GOPAL"
for letter in my_string_continue:
    if letter == 'A':
        continue  # Skip the implementation and go back to the top of the loop
    print(letter)

my_iterator_break = 0
while my_iterator_break < 5:
    if my_iterator_break == 4:
        break
    print(my_iterator_break)
    my_iterator_break += 1
