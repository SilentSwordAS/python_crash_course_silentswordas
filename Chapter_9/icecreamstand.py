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

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavours = ["Blueberry","Mango","Chocolate","Strawberry"]
    
    def display_flavours(self):
        return self.flavours

ics1 = IceCreamStand("Baskin Poppins","Dessert")
print(ics1.flavours)