# Using Break Keyword
while True:
    topping = input("What topping would you like on your pizza? ")
    if topping.lower() == "quit":
        break
    else:
        print(f"You have added {topping} to your pizza.")

# Using the While conditional
topping = input("What topping would you like on your pizza? ")
while topping != "quit":
    print(f"You have added {topping} to your pizza.")
    topping = input("What topping would you like on your pizza? ")

# Using a Flag variable
active = True

while active:
    topping = input("What topping would you like on your pizza? ")
    if topping.lower() == "quit":
        active = False
    else:
        print(f"You have added {topping} to your pizza.")