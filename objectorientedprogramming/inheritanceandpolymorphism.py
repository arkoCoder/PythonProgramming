# Base class
class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating")


# Inheritance
# Child Class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # Overriding the implementation of base class methods
    def who_am_i(self):
        print("I am a DOG")

    def bark(self):
        print("WOFF!")


my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

#Abstract Classes

class BaseClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        raise NotImplementedError("Expecting a child class to provide an implementation")


class ChildClass(BaseClass):
    def say_hello(self):
        return "Hello " + self.name


my_child_class = ChildClass("Gopal")
print(my_child_class.say_hello())
# Below code will throw NotImplementedError
#my_base_class = BaseClass("Gopal")
#my_base_class.say_hello()

