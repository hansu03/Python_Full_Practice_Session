
  #break statement : we can stop loop even conndition  is true    using if
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1





#break using for 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
