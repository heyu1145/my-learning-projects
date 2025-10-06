import bank
while True:
  name = input("Please enter the accounts name:\n")
  if name != "":
    break

while True:
  Error = False
  startmoney = input("Please Input your start money:\n")
  if startmoney != "":
    try:
      int_startmoney = int(startmoney)
    except ValueError:
      print("Please enter a int number!")
      Error = True
    if not Error and int_startmoney >= 0:
      account = bank.Bank(name=name,money=int_startmoney)
      break
    else:
      print("start money is smaller than 0!")

while True:
  print("=" * 20)
  print("status:\n0: exit,\n1: active,\n2: save money,\n3: withdraw money,\n4: Show Info,\n5: Show money,")
  print("=" * 20)
  Choice = input("Please choice with 0-5: ")
  if Choice == "0":
    print("exit……")
    break
  elif Choice == "1":
    print("active")
    account.active()
  elif Choice == "2":
    print("save money")
    while True:
      try:
        save_money = int(input("how many money you want to save: "))
        break
      except ValueError:
        print("Please insert a int number!")
    account.savemoney(save_money)
  elif Choice == "3":
    print("withdraw money")
    while True:
      try:
        withdraw = int(input("how many money you want to withdraw: "))
        break
      except ValueError:
        print("Please insert a int number!")
    account.withdrawmoney(withdraw)
  elif Choice == "4":
    print("Show Info")
    account.showinfo()
  elif Choice == "5":
    print("Show money")
    account.serachmoney()
  else:
    print("Please select in 1-5!")

