#A Class is like an object constructor, or a "blueprint" for creating objects.


#Create a Class
#To create a class, use the keyword class:
#create a class named MyClass, with a property named x:

class MyClass:
  x = 5


#create objects
p1 = MyClass()
print(p1.x)


#use the __init__() function to assign values for name and age
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)





# string function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
p1 = Person("John", 36)
print(p1)





# object method : object can contain methods.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()





#modify object parameter
p1.age = 40


# delete object parameter
del p1.age
