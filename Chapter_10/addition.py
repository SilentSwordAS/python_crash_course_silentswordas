while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == "q":
        break
    second_number = input("Enter the second number: ")
    if second_number.lower() == "q":
        break
    try:
        print(int(first_number)+int(second_number))
    except ValueError:
        print("Please enter numbers for successful addition!")
    