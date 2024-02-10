# practice question
class student:
    def __init__(self,name,marks1, marks2 , marks3):
        self.name = name
        self.average = (marks1 + marks2 + marks3)/3

    def printResult(self):
        print(self.name,"Your average is : ", self.average)

s1 = student("Aboubakar", 90, 80, 70)
s1.printResult()
