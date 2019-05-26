class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def saluda(self):
    print("Hola, me llamo " + self.name + " y tengo" + self.age)