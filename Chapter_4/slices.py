## Exercise 4-10,4-12
slicing_list = ["Margherita pizza","Pepperoni pizza",
                "Neapolitan pizza","Sicilian pizza",
                "Chicago deep-dish pizza","New York-style pizza",
                "Greek pizza","California pizza","Hawaiian pizza"]

# First Three Items
print("The first three items of the list are: ")
for item in slicing_list[:3]:
    print(item)

# The Next Three Items
print("The next three items in the list are:")
for item in slicing_list[3:6]:
    print(item)

# The Last Three Items
print("The last three items in the list are:")
for item in slicing_list[6:]:
    print(item)


## Exercise 4-11

my_pizza = slicing_list[:3]
friends_pizza = slicing_list[:3]

friends_pizza.append("New York-style pizza")
my_pizza.append("Hawaiian pizza")

# Listing out my_pizza
print("My favourite pizzas are: ")
for item in my_pizza:
    print(item)

# Lisiting out friends_pizza
print("My friend's favourite pizzas are: ")
for item in friends_pizza:
    print(item)