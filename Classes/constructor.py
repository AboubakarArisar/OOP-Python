#constructor in the class 


#in constructor self is a reference to the object of the class


class Student:
    name="Aboubakar"
    age=20

#creating a constructor
    def __init__(self):
        print("constructor called")

#creating an object of the class
        
s1=Student()



#creating arguments in the constructor
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("constructor called")

s1=Student("Aboubakar",20)
print(s1.name)
print(s1.age)


#creating a default argument in the constructor
class Student:
    def __init__(self,name="Aboubakar",age=20):
        self.name=name
        self.age=age
        print("constructor called")

s1=Student()


