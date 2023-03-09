#types of operators 




#Arithmetic operators
x = 5
y = 3
print(x + y)




#Assignment Operators   
x = 5
x |= 3
print(x)





#Comparison operators
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3






#Logical operators
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10



 






#Bitwise operators
print(6 & 3)
#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 2 = 0000000000000010
#====================
#Decimal numbers and their binary values:
# 0 = 0000000000000000
# 1 = 0000000000000001
#2 = 0000000000000010
#3 = 0000000000000011
#4 = 0000000000000100
#5 = 0000000000000101
#6 = 0000000000000110
#7 = 0000000000000111
#"""
            







#Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y








#Membership operators
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
