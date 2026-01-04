buffet_foods = ("Rajma Chawal", "Burger", "Pizza", "Momos", "Chowmein")

# Printing each value in the tuple
print("Each item in the original buffet foods: ")
for item in buffet_foods:
    print(item)

# Raising a type error by assigning a different value in the tuple
# buffet_foods[0] = "Pasta"

# Traceback (most recent call last):
#   File "c:\Users\Anuraag Shukla\Downloads\Python_Crash_Course\python_crash_course_silentswordas\Chapter_4\buffet.py", line
#  9, in <module>
#     buffet_foods[0] = "Pasta"
#     ~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment


# Modifying the variable buffet_foods
print("Each item in the modified buffet foods: ")
buffet_foods = ("Rajma Chawal", "Burger", "Pizza","Pasta","Chicken Wings")
for item in buffet_foods:
    print(item)