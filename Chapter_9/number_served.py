class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        return f"Restaurant's name is: {self.name}\nRestaurant's cuisine type is: {self.type}"
    
    def open_restaurant(self):
        return f"{self.name} is open for business!"
    
    def set_number_served(self, num):
        self.number_served = num
    
    def increment_number_served(self, num):
        self.number_served += num

    
r1 = Restaurant("Clover","Continental")
print(f"The number of customers this restaurant has served: {r1.number_served}")

r1.number_served = 50
print(f"The number of customers this restaurant has served: {r1.number_served}")

r1.set_number_served(60)
print(f"The number of customers this restaurant has served: {r1.number_served}")

r1.increment_number_served(60)
print(f"The number of customers this restaurant has served: {r1.number_served}")