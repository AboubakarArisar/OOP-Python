#static method in python

#static method does not take self in the parameter

#creating a class

class student:
    name = "Aboubakar"
    
    #creating a method
    def printname(self):
        print("your name is :",self.name)

    #creating another method
    def printage(self,age):
        print("your age is :",age)
    
    @staticmethod
    def printclass():
        print("this is a static method")

#creating an object of the class
s1 = student()
s1.printname()
s1.printage(23)
s1.printclass()
