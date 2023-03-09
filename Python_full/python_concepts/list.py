#create a list
mylist = ["hansu", "anurag", "paras"]


#list length
mylist = ["hansu", "anurag", "paras"]
print(len(mylist))



#list items - data types
# strings, integers and boolean values


#type()
mylist = ["hansu", "anurag", "paras"]
print(type(mylist))


#list()  constructor
mylist = ["hansu", "anurag", "paras"]
print((mylist))




#access list item
mylist = ["hansu", "anurag", "paras"]
print((mylist[1]))




# change list item
mylist = ["hansu", "anurag", "paras"]
mylist[1] = "kundan"
print(mylist)




#insert items in list
mylist = ["hansu", "anurag", "paras"]
mylist.insert(2,"kundan")
print(mylist)




# to add items we use append()
mylist = ["hansu", "anurag", "paras"]
mylist.append("kundan")
print(mylist)




# expamd list  by  extend()
mylist = ["hansu", "anurag", "paras"]
tropical = ["sumit", "jitendra", "om","nisha" ]
mylist.extend(tropical)
print(mylist)






# remove specified item
mylist = ["hansu", "anurag", "paras"]
mylist.remove("hansu")
print(mylist)




# pop method removes last item
# del keyword also removes specified index
#  The clear() method empties the list.






#loop through index numbers
mylist = ["hansu", "anurag", "paras"]
for i in range(len(mylist)):
  print(mylist[i])







#list comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
#newlist = [expression for item in iterable if condition == True]
mylist = ["hansu", "anurag", "paras"]
mylist = [x.upper() for x in mylist]
print(mylist)






#sort list
mylist = ["hansu", "anurag", "paras"]
mylist.sort()
print(mylist)



#copy list
mylist = ["hansu", "anurag", "paras"]
mylist = mylist.copy()
print(mylist)



#join two list
list1 = ["hansu", "anurag", "paras"]
list2 = [1,2,3]
list3 = list1+list2
print(list3)



#list method..........................

# append() Adds an element at the end of the list

# clear()  Removes all the elements from the list

# copy()    Returns a copy of list

# count()   Returns no. of elements with specified value

# extend()    Add the elements of a list to the end of the current list

# index()   

# insert()   Adds an element at the specified position

# pop()      Removes the element at the specified position

# remove()   moves the item with the specified value

# reverse()   reverse order of the list

# sort()      sorts the lsit











