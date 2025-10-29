# Modifying the list and printing the invitation for the new person.

guest_list = ["Person 1", "Person 2", "Person 3"]

print(f"{guest_list[0]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[1]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[2]}, you have been invited to the dinner party on Tuesday at 7 p.m.")

print(f"\n{guest_list[1]} cannot make it to the party.\n")

guest_list[1] = "Person 4"

print(f"{guest_list[0]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[1]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[2]}, you have been invited to the dinner party on Tuesday at 7 p.m.")


