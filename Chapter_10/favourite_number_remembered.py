import json

def get_favourite_number():
    filename = "fav_num.json"
    try:
        with open(filename) as f:
            load_num = json.load(f)
    except FileNotFoundError:
        fav_num = input("Please enter your favourite number: ")
        with open(filename, "w") as f:
            json.dump(fav_num,f)
        return f"I remember your favourite number now!"
    else:
        return f"I know your favourite number! It's {load_num}"

print(get_favourite_number())

