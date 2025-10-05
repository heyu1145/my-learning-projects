
import uuid
from typing import Tuple,Optional
class Bank:
  def __init__(self,name: str,money: int):
    self.name = name
    self.money = money
    self.actived = False
    self.id = uuid.uuid4().hex[:6]
    self.password = None

  def active(self):
    if self.actived:
      print("You had actived,dont active again!")
      return

    while not self.actived:
      Input = input("Please input your 8-digit password or say quit to exit\n")
      if Input == "quit":
        print("Password didnt set! Please try again by restart active!")
        return
      if not Input.isdigit() or len(Input) != 8:
        print("Please insert a 8-digit number!")
      else:
        CurrentPassword = Input
        while not self.actived:
          Input = input("Please enter you password again\n")
          if Input == "quit":
            print("Password didnt set! Please try again by restart active")
            break

          if Input == CurrentPassword:
            self.password = CurrentPassword
            print("Password set!")
            self.actived = True
          else:
             print("Didnt match!")
    print(f"Bank account {self.name}(account id: {self.id}) has been actived! status: ({self.actived})")

  def showinfo(self):
    print("Account Info:")
    print(f"Account name: {self.name}")
    print(f"Account ID: {self.id}")
    print(f"Actived: {self.actived}")

  def savemoney(self,money: int) -> Tuple[bool, Optional[str]]:
    if not self.actived:
      print("Please active first!")
      return False,"didnt active"

    Login = False
    while not Login:
      user_Password = input("Please insert your password(or enter quit to exit): \n")
      if user_Password == "quit":
        print("Login failed!")
        return False, "login failed"
      if user_Password == self.password:
        print("Login!")
        Login = True

    if not money or money < 0:
      print("The number cant be empty!")
      return False,"invalid input"

    self.money += money
    print(f"Saved! Money: {self.money}")
    return True, None

  def withdrawmoney(self,money : int) -> Tuple[bool, Optional[str]]:
    if not self.actived:
      print("Please active first!")
      return False,"didnt active"

    Login = False
    while not Login:
      user_password = input("Please insert your password(or enter quit to exit): \n")
      if user_password == "quit":
        print("Login Failed!")
        return False, "login failed"
      if user_password == self.password:
        print("Login!")
        Login = True

    if not money or money < 0:
      print("The number cant be empty!")
      return False,"invalid input"

    if money > self.money:
      print("You dont have enough money!")
      return False,"no enough money"

    self.money -= money
    print(f"Withdrawed! Money: {self.money}")
    return True, None

  def serachmoney(self):
    print(f"money: {self.money}")

