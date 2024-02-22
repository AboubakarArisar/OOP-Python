#multiple inheritence in python

class A:
    varA = "Welcome to A class"

class B:
    varB = "Welcome to B class"

class C(A,B):
    varC = "Welcome to C class"


obj = C()
print(obj.varA)
print(obj.varB)
print(obj.varC)
