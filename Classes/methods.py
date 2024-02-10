#methods in the classes

#creating a class
class student:
    name = "Aboubakar"
    
    #creating a method
    def printname(self):
        print("your name is :",self.name)

    #creating another method
    def printage(self,age):
        print("your age is :",age)

        

#creating an object of the class
s1 = student()
s1.printname()
