while True:
    response = input("Why do you like programming? ")
    if response.lower() == "quit":
        break
    else:
        with open("poll_responses.txt","a") as file_obj:
            file_obj.write(f"{response}\n")