# Exercises 5-8 and 5-9
users = ["admin","senku_lite", "phantombladexr", "voidfire", "gotyousucker3","que_ota"]
users = []
if users == []:
    print("We need to find some users!")
else:
    for user in users:
        if user == "admin":
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again!")
