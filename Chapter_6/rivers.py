rivers = {
    "nile": "Egypt",
    "amazon": "Brazil",
    "yangtze": "China",
}

for key, value in rivers.items():
    print(f"The river {key.title()} flows through {value}.")

print("\nRivers in the provided dictionary:")
for key in rivers.keys():
    print(f"{key.title()}")

print("\nCountries through which they flow:")
for value in rivers.values():
    print(f"{value}")