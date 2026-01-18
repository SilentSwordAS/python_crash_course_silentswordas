while True:
    topping = input("What topping would you like on your pizza? ")
    if topping.lower() == "quit":
        break
    else:
        print(f"You have added {topping} to your pizza.")