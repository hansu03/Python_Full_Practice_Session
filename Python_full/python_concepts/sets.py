#Sets are used to store multiple items in a single variable.

myset = {"hansu", "sumit", "jitendra"}
print(myset)

# in sets no dulpicates are allowed

# get length of a set
myset = {"hansu", "sumit", "jitendra"}
print(len(myset))


#set data types
myset = {"hansu", "10", "jitendra", "45"}
print(myset)


#type set
myset = {"hansu", "sumit", "jitendra"}
print(type(myset))



#access data 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#add items to set
myset = {"hansu", "sumit", "jitendra"}
myset.add("anurag")
print(myset)


#remove item from set
myset = {"hansu", "sumit", "jitendra"}
myset.discard("jitendra")
print(myset)



#del leyword will delete set completely



#join two sets using union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)




#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)



