current_users = ["senku_lite", "phantombladexr", "que_ota", "voidfire","gotyousucker3"]
new_users = ["phantomblaDEXr", "qUIZzling", "seNKu_lite","Mozzi","K-eyes"]

for user in new_users:
    if user.lower() in current_users:
        print("You will need to enter a new username!")
    else:
        print("This username is available!")

