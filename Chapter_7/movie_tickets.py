while True:
    age = int(input("Enter your age to calculate the ticket price: "))

    if age < 3 and age > 0:
        print("Your ticket is free of cost.")
    elif age >= 3 and age <= 12:
        print("You need to pay 10$ at the counter.")
    elif age > 12:
        print("You need to pay 15$ at the counter.")
    elif age == -1:
        break
    elif age <= 0:
        print("You need to enter a valid age.")