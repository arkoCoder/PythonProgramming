# lambdas are a way of creating one time use anonymous functions
# map function takes in a function and list to apply that function to
# filter function takes in a function and list to apply the filter of that function to
def square_num(num):
    return num ** 2


def check_even(num):
    return num % 2 == 0


my_list = [1, 2, 3, 4]
my_tuple = (1, 2)
print(list(map(square_num, my_list)))
for item in map(square_num, my_tuple):
    print(item)

print(list(filter(check_even, my_list)))

for item in filter(check_even, my_list):
    print(item)

print("Lambdas!!")
print(list(map(lambda num: num ** 2, my_list)))
print(list(filter(lambda num: num % 2 == 0, my_tuple)))

# LEGB Rule for scope of variables:
# Local: Names assigned in any way within the function and not declared global in that function
# Enclosing function locals: Names in the local scope of any and all enclosing functions, from inner to outer
# Global: Names assigned at the top level of module file or declared global in a def within the file
# Built-in: Names preassigned in the built-in names module: open, range etc
x = 50


def global_var():
    global x
    print(f"X is {x}")
    x = 200
    print(f"Local X is {x}")


global_var()
print(f"Global X is {x}")
