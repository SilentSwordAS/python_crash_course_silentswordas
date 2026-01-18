favorite_numbers = {
    "Anuraag":[1,3,33],
    "Mukul": [33,3,1],
    "Mridul": [99,1],
    "Rishabh": [0],
    "John": [22,37],
}

for user, numbers in favorite_numbers.items():
    print(f"\n{user}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")