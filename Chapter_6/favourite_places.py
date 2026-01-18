favourite_places = {
    "Anuraag": ["Ambala", "Ahmedabad", "Shimla"],
    "John": ["New Jersey","New York","Austin"],
    "Jane": ["Los Angeles","Las Vegas","Rio De Janeiro"],
}

for user, places in favourite_places.items():
    print(f"\n{user}")
    for place in places:
        print(f"\t{place}")