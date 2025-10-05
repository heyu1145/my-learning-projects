import math
print("Hello!")
try:
    Input = float(input("Please enter a number: "))
except ValueError:
    print("Invalid input!")
    exit()

A = round(Input%2,10)
isOdd = False
if A == 0:
  print(f"The number is Even")
elif A == 1:
  print(f"The number is Odd")
  isOdd = True
else:
  print(f"The number is Decimal,Remainder: {A}")

isPositive = False
if Input > 0:
  rt = math.sqrt(Input)
  isPositive = True
  print(f"The number has two roots: {rt} and {-rt}")
elif Input == 0:
  print(f"The number has one root: 0")
else:
  print(f"The number doesnt have real root")
  rt = math.sqrt(-Input)
  print(f"Two of Imaginary roots: {rt}i and {-rt}i")
Int_Input = int(Input)
if Int_Input == 2:
  print("The number is a prime")
elif Int_Input == 1:
  print("The number is NOT a prime")
elif isOdd and isPositive:
  match = None
  for i in range(3,math.isqrt(Int_Input)+1,2):
    if Int_Input%i == 0:
      print("The number is NOT a prime")
      match = i
      break
  if match == None:
    print("The number is a prime")
else:
  print("The number is NOT a prime")
