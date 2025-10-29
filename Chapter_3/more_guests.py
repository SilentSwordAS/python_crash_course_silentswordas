# Further Modifications of the Code to insert elements at certain indices 

guest_list = ["Person 1", "Person 2", "Person 3"]

print(f"{guest_list[0]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[1]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[2]}, you have been invited to the dinner party on Tuesday at 7 p.m.")

print(f"\n{guest_list[1]} cannot make it to the party.\n")

guest_list[1] = "Person 4"

print(f"{guest_list[0]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[1]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[2]}, you have been invited to the dinner party on Tuesday at 7 p.m.")

print(f"\nGood News! We found a bigger dinner table\n")

guest_list.insert(0, "Albert")
guest_list.insert(len(guest_list)//2, "Bill")
guest_list.append("Max")

print(f"{guest_list[0]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[1]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[2]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[3]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[4]}, you have been invited to the dinner party on Tuesday at 7 p.m.")
print(f"{guest_list[5]}, you have been invited to the dinner party on Tuesday at 7 p.m.")

