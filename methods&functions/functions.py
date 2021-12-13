# functions in python allows to create blocks of code that can be easily executed many times without needing to
# rewrite entire block
# def keyword is used to create a function. function names basically uses snakes casing.
# Snake casing is all lowercase with underscores between words
# docstring is used to describe a function and is a multiline commented description between ''' ''''
'''
Docstring to describe function
'''


def first_function():
    print("Hello Functions!")


def function_with_arg(name):
    print(f"Hello {name}")


def function_with_arg_with_default_value(name="NoName"):
    print(f"Hello {name}")


def function_with_return(num1, num2):
    return num1 + num2


def function_for_tuple_unpacking(tuple_list):
    for employee, wrk_hrs in tuple_list:
        print(f"Employee {employee} work for {wrk_hrs}")


def function_with_args(
        *args):  # Here args is a tuple of the parameters passed on.The * symbol indicates that there is no limit for parameters count
    return sum(args)


def function_with_kwargs(**kwargs):  # Here kwargs is a dictionary of the paramaters passed on.
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"Found fruit here {kwargs['fruit']}")
    else:
        print("No fruit found")


def function_with_args_and_kwargs(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs['food']))


first_function()
function_with_arg("Gopal")
result = function_with_return(1, 2)
print(result)
function_with_arg_with_default_value()
function_for_tuple_unpacking([("Gopal", 10), ("Harsh", 20)])
sum_of_numbers = function_with_args(1, 2, 3)
print(sum_of_numbers)
function_with_kwargs(fruit="apple", veggie='lettuce')
function_with_args_and_kwargs(10, food='oranges')

outputString = ''
inputString = "Gopal"
for index, letter in enumerate(inputString):
    if index % 2 == 0:
        outputString += letter.lower()
    else:
        outputString += letter.upper()
print(outputString)
my_list = [1, 2, 3]
for index, num in enumerate(my_list):
    print(index , num)
