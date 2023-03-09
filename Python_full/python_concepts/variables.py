#creating variable
x = 678
y = "Hansu"
print(x)
print(y)




#get type 
x = 678
y = "Hansu"
print(type(x))
print(type(y))




#single or double quotes
y = "Hansu"
# is same as
y = 'Hansu'




#Variables name can be written in of below form 
myvar = "Hansu"
my_var ="Hansu"
_my_var = "Hansu"
myVar = "Hansu"
MYVAR = "Hansu"
myvar2 ="Hansu"




#One Value to Multiple Variables
x = y = z = "Hansu"
print(x)
print(y)
print(z)



#Output Variables
x = " My name is Hansu"
print(x)



#Global Variables......................Variables that are created outside of a function (as in all of the examples above) are known as global variables.Global variables can be used by everyone, both inside of functions and outside.
x = "Hansu"
def myfunc():
    global x
    x="Hansu"
    
myfunc()
  print("My name is  " + x)













