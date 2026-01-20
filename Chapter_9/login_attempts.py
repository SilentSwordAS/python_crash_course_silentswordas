class User:
    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0
    
    def describe_user(self):
        return {
            "full_name": self.fname+" "+self.lname,
            "age": self.age,
            "nationality": self.nationality,
        }
    
    def greet_user(self):
        return f"Hi {self.fname}! How are you doing this fine day?"

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

u1 = User("John","Doe",32,"American")

for _ in range(5):
    u1.increment_login_attempts()

print(u1.login_attempts)

u1.reset_login_attempts()
print(u1.login_attempts)