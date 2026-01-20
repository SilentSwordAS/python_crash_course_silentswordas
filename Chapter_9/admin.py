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

class Admin(User):
    def __init__(self,fname,lname,age,nationality):
        super().__init__(fname,lname,age,nationality)
        self.privileges = ["can add post","can delete post","can ban user"]
    
    def show_privileges(self):
        return self.privileges

a1 = Admin("Jack","Frost","25","Mexican")
print(a1.show_privileges())