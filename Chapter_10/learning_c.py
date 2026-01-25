# Storing the lines as a list using 'readlines' method
with open("./learning_python.txt") as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.strip().replace("Python","C"))