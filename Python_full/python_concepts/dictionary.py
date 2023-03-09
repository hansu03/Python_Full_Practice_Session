#Create and print a dictionary:
mydict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)


#duplicate not allowed


#dictionary length
print(len(mydict))



#dictionary datatype
#type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


# change and get values
# get values: The values() method will return a list of all the values in the dictionary.

#The keys() method will return a list of all the keys in the dictionary.










# change values
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict["year"] = 2018




#update dictionary
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict.update({"year": 2020})
print(thisdict)




#remove items
mydict.pop("model")
print(mydict)









#nested dictionary: dictionary can contain dictionary
myfamily = {
  "child1" : {
    "name" : "jitendra",
    "year" : 2004
  },
  "child2" : {
    "name" : "om",
    "year" : 2005
  },
  "child3" : {
    "name" : "anurag",
    "year" : 2006
  }
}

print(myfamily)
