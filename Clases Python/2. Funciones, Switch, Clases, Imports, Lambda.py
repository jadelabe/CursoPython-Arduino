#matrices

#Functions
def my_function():
  print("Hello from a function")

my_function()

#return

#switch
def week(i):
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
        }
    return switcher.get(i,"Invalid day of week")


week(3)

#Clases
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
del p1.age
del p1

#Child Class
class Student(Person):
  def __init__(self, name, age, year):
    Person.__init__(self, name, age)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.name, "to the class of", self.graduationyear)


#importing
from clase2 import Person
from include.person import Person

#Extra 

#Lambda
#A lambda function can take any number of arguments, but can only have one expression.

#lambda arguments : expression
#x = lambda a : a + 10
#x = lambda a, b : a * b
#