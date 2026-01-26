try:
    with open("./cats.txt") as file_obj:
        for line in file_obj:
            print(line.strip())

    with open("./dogs.txt") as file_obj:
        for line in file_obj:
            print(line.strip())
except FileNotFoundError:
    # print("One of the files required does not exist or has been moved.") ## Exercise 10-8
    pass
