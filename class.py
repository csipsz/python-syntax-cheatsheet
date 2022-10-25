class Employee:
  def __init__(self, name):
    self.name = name

  def __repr__(self): #string representation of the class. one parameter, self, should return a string
    return self.name

tim = Employee('Tim')
print(tim) # John

class Dog:
  def bark(self):
    print("woof")

spike = Dog()
spike.bark()


class Car:
  "This is an empty class"
  pass

honda = Car()

class my_class:
  class_variable = "I am a Class Variable!"
  
x = my_class()
print(my_class.class_variable) #I am a Class Variable!
print(x.class_variable) #I am a Class Variable!


class Animal:
  def __init__(self, voice):
    self.voice = voice

cat = Animal('Meow')
print(cat.voice) # Output: Meow

dog = Animal('Woof') 
print(dog.voice) # Output: Woof



class Mammal:
  def __init__(self, name, number_of_legs):
    self.name = name
    self.number_of_legs = number_of_legs

#built-in dir() function with no arguments, returns a list of all the attributes in the current scope
#with object as argument returns object attributes

class Employee:
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print("Hi, I'm " + self.name)


print(dir())
# ['Employee', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'new_employee']

print(dir(Employee))
# ['__doc__', '__init__', '__module__', 'print_name']

#__main__ is an identifier to reference the current file context. When a module is read from standard input, a script, or from an interactive prompt, its __name__ is set equal to __main__.

#create an instance of class CoolClass printing the type:
#<class '__main__.CoolClass'>
#because class CoolClass was defined in the current script file.

