people = [{
    "first_name":"Anuraag",
    "last_name":"Shukla",
    "age": 23,
    "city":"Ambala"
}, {
    "first_name":"John",
    "last_name":"Doe",
    "age": 30,
    "city":"Los Angeles"
},
{
    "first_name":"Jane",
    "last_name":"Doe",
    "age": 40,
    "city":"Las Vegas"
}]

for person in people:
    print(f"\nFull Name: {person['first_name']+" "+person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")