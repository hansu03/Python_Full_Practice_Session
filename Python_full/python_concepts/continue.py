#continue : With the continue statement we can stop the current iteration, and continue with the next:
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)




#continue using for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
