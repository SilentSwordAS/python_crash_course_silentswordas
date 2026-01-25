while True:
    name = input("Please enter your name: ")
    if name.lower() == "quit":
        break
    else:
        with open("guest_book.txt","a") as file_obj:
            print(f"Hi {name}!")
            file_obj.write(f"{name}\n")