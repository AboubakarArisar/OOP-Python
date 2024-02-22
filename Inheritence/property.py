#@property decorator in python

class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @property
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

print(harry.printdetails)
print(rohan.printdetails)

