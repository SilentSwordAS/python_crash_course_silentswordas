# Exercise 5-1 and 5-2

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

car = "subaru"
print("Is car == 'Subaru'? I predict False.")
print(car == "Subaru")

game = "Silksong"
print("Is game == 'Silksong'? I predict True")
print(game == "Silksong")

game = "Cyberpunk 2077"
print("Is game == 'Silksong'? I predict False")
print(game == "Silksong")

game = "Cyberpunk 2077"
print("Is game.lower() == 'cyberpunk 2077'? I predict True")
print(game.lower() == "cyberpunk 2077")

game = "Cyberpunk 2077"
print("Is game == 'cyberpunk 2077'? I predict False")
print(game == "cyberpunk 2077")

game = "The Witcher 3: Wild Hunt"
print("Is game != 'Silksong'? I predict True")
print(game != "Silksong")

game = "The Witcher 3: Wild Hunt"
print("Is game != 'The Witcher 3: Wild Hunt'? I predict False")
print(game != "The Witcher 3: Wild Hunt")

# Numerical Tests

print("Is 67 >= 50 and >=90? I predict False")
print((67>=90) and (67>=50))

print("Is 67 >= 50 or >=90? I predict True")
print((67>=90) or (67>=50))

# Membership Tests

toppings = ["baby corns","anchovies","mushrooms"]

print("Is 'anchovies' in toppings? I predict True")
print("anchovies" in toppings)

print("Is 'pepperoni' in toppings? I predict False")
print("pepperoni" in toppings)

print("Is 'anchovies' not in toppings? I predict False")
print("anchovies" not in toppings)

print("Is 'pepperoni' not in toppings? I predict True")
print("pepperoni" not in toppings)

