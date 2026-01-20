class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        return f"Restaurant's name is: {self.name}\nRestaurant's cuisine type is: {self.type}"
    
    def open_restaurant(self):
        return f"{self.name} is open for business!"


res = Restaurant("Clove","Continental")

print(res.name)
print(res.type)
print(res.describe_restaurant())
print(res.open_restaurant())

res2 = Restaurant("USA Gardens","Indian")

print(res2.describe_restaurant())

res3 = Restaurant("Crystal Gardens","Chinese")

print(res3.describe_restaurant())