# Add these methods to class student - full_name, year_of_birth, initials. 
# Create two instances and verify the work as expected

class Student:
        school="AkiaChix"
        def __init__(self,first_name,last_name,age,country):
         self.first_name=first_name
         self.last_name=last_name
         self.age=age
         self.country=country
         
        def full_name(self):
            return f"{self.first_name} {self.last_name} is your full name"
        def greet(self):
            return f"Hello {self.first_name} {self.last_name} you are from {self.country} welcome to {self.school}"
        def year_of_birth(self):
            year=2022-self.age
            return f" You were born in {year}"
        def initial(self):
            return f"Your initials are {self.first_name[0]}{self.last_name[0]}"
             