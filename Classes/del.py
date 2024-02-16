#del keyword in python
#for deleting any attribute of an object or the object itself, we use del keyword






class Program:
    def __init__(self):
        self.name = "Python"
        self.version = 3.8
        self.company = "Python Software Foundation"
        
    def show(self):
        print(f"Name: {self.name}\nVersion: {self.version}\nCompany: {self.company}")
        
    def __del__(self):
        print("Object has been deleted")

p = Program()
p.show()
del p
print(p) #Error: NameError: name 'p' is not defined
