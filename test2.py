import math
print("Hello!\n")
try:
    Input = float(input("Please enter a number: "))
except ValueError:
    print("Invalid input!")
    exit()

A = round(Input%2,10)
if A == 0:
  print(f"The number is Even\n")
elif A == 1:
  print(f"The number is Odd\n")
else:
  print(f"The number is Decimal,Remainder: {A}\n")

if Input > 0:
  rt = math.sqrt(Input)
  print(f"The number has two roots: {rt} and {-rt}")
elif Input == 0:
  print(f"The number has one root: 0")
else:
  print(f"The number doesnt have real root\n")
  rt = math.sqrt(-Input)
  print(f"Two of Imaginary roots: {rt}i and {-rt}i")
