#Tuples are used to store multiple items in a single variable.


#create a tuple
mytuple = ("hansu", "sumit", "anurag" )
print(mytuple)


#tuple length
mytuple = ("hansu", "sumit", "anurag" )
print(len(mytuple))


#A tuple can contain different data types:
tuple = ("hansu", 22, "male")



#type of tuple
mytuple = ("hansu", "sumit", "anurag" )
print(type(mytuple))




#acess tuple items
mytuple = ("hansu", "om", "jitendra")
print(mytuple[1])



#range of index
mytuple = ("hansu", "om", "jitendra", "sumit", "anurag")
print(mytuple[2:5])




# Change Tuple Values
# once tuple created we cannot change its values  . But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.





#packing a tuple
mytuple = ("hansu", "sumit", "anurag" )
print(mytuple)




#unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)





#join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)










# count() : returns teh no. of times a specified value occurs in tuple

# index() : Searches the tuple for a specified value and returns the position of where it was found


