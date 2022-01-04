class MyFirstClass:
    # CLASS OBJECT ATTRIBUTES are same for any instance of the class
    profession = "Staff Software Engineer"

    # Constructor for the class
    def __init__(self, fname, mname, lname):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def printMessage(self):
        print(f"Hello {self.fname} {self.mname} {self.lname} with post {MyFirstClass.profession}")


my_first_class = MyFirstClass(fname="Gopal", mname="Anil", lname="Heda")
my_first_class.printMessage()
