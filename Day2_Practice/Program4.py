#else is called
x=1
while x<5:
  x=x+1
  print(x)
else:
  print("else is invoked") 


# else is not called
x=1
while x<5:
  x=x+1
  print(x)
  break
else:
  print("else is invoked") 