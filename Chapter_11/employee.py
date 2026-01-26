class Employee():
    def __init__(self,fname,lname,salary):
        self.first_name = fname
        self.last_name = lname
        self.salary = salary
    
    def give_raise(self, increment=5000):
        self.salary += increment
        