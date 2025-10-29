# Using every single method learnt

countries = ["India","China","United States Of America","Israel","Australia"]


# Append
countries.append("Brazil")
print(countries)

# Insert
countries.insert(0, "Canada")
print(countries)

# Pop
popped_item = countries.pop()
print(popped_item)
print(countries)

# Remove
countries.remove("China")
print(countries)

# Sort
countries.sort()
print(countries)

# Sorted
print(sorted(countries, reverse=True))

# Reverse
countries.reverse()
print(countries)

# Len
print(len(countries))


