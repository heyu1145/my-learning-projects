try:
        user_input = input("Please enter a number: ")
            if user_input == "":
                        print("Please input a number!")
                            else:
                                        number = int(user_input)
                                                for i in range(1, number + 1):
                                                                print(i)
except ValueError:
        print("Please input a valid number!")
