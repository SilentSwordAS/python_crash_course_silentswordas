unfinished_sandwiches = ["Grilled cheese","Tomato cucumber","Egg mayo","Corn cheese","Pastrami"]
finished_sandwiches = []

while unfinished_sandwiches:
    prepared_sandwich = unfinished_sandwiches.pop()
    print(f"I have prepared your {prepared_sandwich} sandwich.")
    finished_sandwiches.append(prepared_sandwich)