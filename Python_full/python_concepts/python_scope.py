#  A variable is only available from inside the region it is created. This is called scope.



#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = 300
  print(x)
myfunc()




# Global Scope : A variable created in the main body of the Python code is a global variable and belongs to the global scope.
x = 300
def myfunc():
  print(x)
myfunc()
print(x)




#Global Keyword
def myfunc():
  global x
  x = 300
myfunc()
print(x)
