pets = [
    {
    "name": "Brock",
    "kind":"Dog",
    "owner":"Anuraag",
    },
    {
    "name": "Dodge",
    "kind":"Sea Lion",
    "owner":"John",
    },
    {
    "name": "Sparkles",
    "kind":"Cat",
    "owner":"Jane",
    },
]

for pet in pets:
    print(f"\nName of the pet: {pet['name']}")
    print(f"Type of Animal: {pet['kind']}")
    print(f"Owner of the pet: {pet['owner']}")
