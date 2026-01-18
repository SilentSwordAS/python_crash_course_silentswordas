def prepare_sandwich(*toppings):
    print("Preparing a sandwich with the following toppings: ")
    for t in toppings:
        print(f"-{t}")

prepare_sandwich("lettuce", "tomato")
prepare_sandwich("mayonnaise", "cream cheese", "guacamole")
prepare_sandwich("pickles", "roasted red peppers", "jalapeños", "sun-dried tomatoes",)