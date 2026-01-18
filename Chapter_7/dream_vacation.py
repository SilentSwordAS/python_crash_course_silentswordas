polling = True
poll_results = {}
while polling:
    name = input("Please enter your full name: ")
    response = input("\nIf you could visit one place in the world, where would you go? ")
    poll_results[name] = response
    continue_poll = input("Would you like to add another responder to the poll? (Yes/No) ")
    if continue_poll == "No":
        polling = False

for key in poll_results:
    print(f"{key} wants to visit {poll_results[key]}!")
