import random
ticket_list = [42, 17, 89, 33, 76, 5, 91, 28, 64, 12, 'K', 'R', 'P', 'M', 'X']

my_ticket = ""
for _ in range(4):
    my_ticket += str(random.choice(ticket_list))

print(f"Any ticket matching these 4 numbers or letters wins the prize: {my_ticket}")

count=0

cust_ticket = ""
while cust_ticket != my_ticket:
    count += 1
    cust_ticket = ""
    for _ in range(4):
        cust_ticket += str(random.choice(ticket_list))

print(count)
    
