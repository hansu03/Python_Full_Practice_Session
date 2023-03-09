#Write a program to demonstrate working with dictionaries in python. 


# create a dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)



# Add Elements to a Python Dictionary
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)





#Accessing Elements from Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters










#Removing elements from Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)