import random
class Dice():
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)

d1 = Dice()
print("6 Sided Dice")
for _ in range(10):
    print(d1.roll_die())

print("\n10 Sided Dice")
d2 = Dice(10)
for _ in range(10):
    print(d2.roll_die())

print("\n20 Sided Dice")
d3 = Dice(20)
for _ in range(10):
    print(d3.roll_die())