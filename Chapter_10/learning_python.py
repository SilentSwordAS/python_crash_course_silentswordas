# Reading the complete file using the 'read' method 
with open("learning_python.txt") as file_obj:
    content = file_obj.read()
    print(content.strip())
    print("---------------------------------------------")
# Looping through each line with a for loop over the file_obj
with open("./learning_python.txt") as file_obj:
    for line in file_obj:
        print(line.strip())
    print("---------------------------------------------")
# Storing the lines as a list using 'readlines' method
with open("./learning_python.txt") as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.strip())
print("---------------------------------------------")

