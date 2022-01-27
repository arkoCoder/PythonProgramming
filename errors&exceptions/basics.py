# try except and finally blocks are used for error handling in python.
try:
    result = 10 + 10
except TypeError:
    print("Something is fishy!!")
else:
    print("All Good!")
finally:
    print("I will always run no matter what")

print("Bella Ciao!! ")
