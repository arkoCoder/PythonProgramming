# open function is used to open file from a certain path provided
# read function is used to read the content of the file. It returns the file data in string format
# readlines function is used to read the content of the file. It returns the file data in list format
# seek function is used to seek the pointer to start of the file.This should be used once you have read the file content
# close function should be used to close the file

with open('test.txt', mode='w') as my_file:
    my_file.write('Hello World')

with open('test.txt', mode='r') as my_file:
    print(my_file.read())

