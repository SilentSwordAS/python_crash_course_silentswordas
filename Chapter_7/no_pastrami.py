unfinished_sandwiches = ["Grilled cheese","Tomato cucumber","Pastrami","Egg mayo","Pastrami","Corn cheese","Pastrami"]
finished_sandwiches = []

print("The restaurant has run out of Pastrami.")
while "Pastrami" in unfinished_sandwiches:
    unfinished_sandwiches.remove("Pastrami")

while unfinished_sandwiches:
    prepared_sandwich = unfinished_sandwiches.pop()
    print(f"I have prepared your {prepared_sandwich} sandwich.")
    finished_sandwiches.append(prepared_sandwich)