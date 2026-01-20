class User:
    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality
    
    def describe_user(self):
        return {
            "full_name": self.fname+" "+self.lname,
            "age": self.age,
            "nationality": self.nationality,
        }
    
    def greet_user(self):
        return f"Hi {self.fname}! How are you doing this fine day?"

u1 = User("John","Doe",32,"American")

print(u1.describe_user())
print(u1.greet_user())

u2 = User("Jane","Doe",27,"Indian")

print(u2.describe_user())
print(u2.greet_user())