class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  # Use the Person class to create an object, and then execute the printname method:

  def myfunc(self):
    print("Hello my name is " + self.firstname + ' ' + self.lastname)

x = Person("John", "Doe")
x.printname()

print(x.firstname)
print(x.lastname)
print(x.firstname, x.lastname)

x.myfunc()
